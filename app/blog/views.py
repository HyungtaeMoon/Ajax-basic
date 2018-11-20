from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Post, Comment


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_post_list.html']
        return ['blog/index.html']


index = PostListView.as_view()

post_create = CreateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')


# post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:index'))

# 위의 post_delete CBV 를 아래와 같이 상속받아 가독성을 높일 수 있다.
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


post_delete = PostDeleteView.as_view()


class CommentCreateView(CreateView):
    model = Comment
    fields = ['message']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url(self.object.post)


comment_create = CommentCreateView.as_view()


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['message']

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

    post_list = []
    for post in qs:
        post_list.append({'id': post.id, 'title': post.title, 'content': post.content})
    # JsonResponse 의 default는 dict 이기 때문에 False 로 설정
    return JsonResponse(post_list, safe=False)
