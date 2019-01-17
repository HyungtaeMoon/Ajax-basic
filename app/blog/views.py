from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, resolve_url
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .forms import CommentForm
from .models import Post, Comment
from .serializers import PostSerializer


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_post_list.html']
        return ['blog/index.html']


index = PostListView.as_view()

post_create = CreateView.as_view(model=Post, fields='__all__')


class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context):
        if self.request.is_ajax():
            return JsonResponse({
                'title': self.object.title,
                'summary': truncatewords(self.object.content, 100),
            })
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        # get_context_data 의 context 에 CommentForm 을 정의
        # 해당 메서드가 없을 경우, 유효하지 않은 폼이라는 에러 메시지 발생
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


post_detail = PostDetailView.as_view()

post_edit = UpdateView.as_view(model=Post, fields='__all__')


# post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:index'))

# 위의 post_delete CBV 를 아래와 같이 상속받아 가독성을 높일 수 있다.
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


post_delete = PostDeleteView.as_view()


class CommentListView(ListView):
    model = Comment

    def get_queryset(self):
        # super() 가 없을 경우,
        # get_queryset 이 재귀함수로 실행되어 스택오버플로우 발생
        qs = super().get_queryset()
        # qs.filter 로 post_pk 값을 post__id 로 qs 변수에 할당
        # 모든 comment 를 보여주는 것이 아닌
        #  post id 에 해당하는 comment 만 가져옴
        qs = qs.filter(post__id=self.kwargs['post_pk'])

        latest_comment_id = self.request.GET.get('latest_comment_id', None)
        if latest_comment_id:
            qs = qs.filter(id__gt=latest_comment_id)
        # return 되는 값은 해당 post 에 해당하는 comment 들
        return qs


# commentListView 를 urls.py 에서보다
# views.py 에서 정의하는 것이 보기 편하여 이와 같이 정의
comment_list = CommentListView.as_view()


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        # return super().form_valid(form)
        response = super().form_valid(form)

        # request 가 ajax 일 때만 처리
        if self.request.is_ajax():
            context = {
                'comment': comment,
            }
            return render(self.request, 'blog/_comment.html', context)

        return response

    def get_success_url(self):
        return resolve_url(self.object.post)

    def get_template_names(self):
        # ajax 로 처리된 html 과 단순 form 으로 처리하는 두가지 방향
        if self.request.is_ajax():
            # ajax 처리를 하면 _comment_form 템플릿으로 처리
            return ['blog/_comment_form.html']
        # 그게 아니면 comment_form 템플릿으로 처리
        return ['blog/comment_form.html']


comment_create = CommentCreateView.as_view()


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return resolve_url(self.object.post)


comment_edit = CommentUpdateView.as_view()


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return resolve_url(self.object.post)


comment_delete = CommentDeleteView.as_view()


def post_list_json(request):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)
    json_utf8_string = JSONRenderer().render(serializer.data)
    # content_type 은 명시하는 것일뿐 파일의 형식이 바뀌는 것은 아니다.
    return HttpResponse(json_utf8_string, content_type='application/json; charset=utf-8')
