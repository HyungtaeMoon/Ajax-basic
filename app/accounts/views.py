from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView


class SignupForm(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL

    def form_valid(self, form):
        #
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'next_url': self.get_success_url()})
        return response

    def get_template_names(self):
        if self.request.is_ajax():
            return ['accounts/_signup_form.html']
        return ['accounts/signup_form.html']


# login_required 데코레이터를 사용하지 않으면,
#   accounts/login/?next=/accounts/profile/ 로 리다이렉트 시킨다
@login_required
def profile(request):
    # login 을 하면서 request 에 유저의 정보가 담겨있기 때문에 render 로
    #   request 와 template 만 지정
    return render(request, 'accounts/profile.html')


class LoginForm(AuthLoginView):
    def form_valid(self, form):
        if self.request.is_ajax():
            # POST 요청을 통해 들어온 form 데이터
            response = super().form_valid(form)
            if self.request.is_ajax():
                # 템플릿의 ajax 처리 부분에서 response.next_url 로 데이터를 보냄
                return JsonResponse({'next_url': self.get_success_url()})
            return response

    def get_template_names(self):
        if self.request.is_ajax():
            # ajax 처리로 들어오면 modal 폼을 띄우고
            return ['accounts/_login.html']
        # url 로 get 요청하면 단순 login.html 페이지를 보여줌
        return ['accounts/login.html']
