from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class SignupForm(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL


# login_required 데코레이터를 사용하지 않으면,
#   accounts/login/?next=/accounts/profile/ 로 리다이렉트 시킨다
@login_required
def profile(request):
    # login 을 하면서 request 에 유저의 정보가 담겨있기 때문에 render 로
    #   request 와 template 만 지정
    return render(request, 'accounts/profile.html')
