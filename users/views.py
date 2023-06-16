from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic import FormView

from users.forms import RegisterForm, LoginForm
from users.models import Users
from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html', {'user' : request.session.get('user')})
    #return render(request, 'shop/index.html'



'''
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        re_password = request.POST.get('re-password', '')

        # 전송할 데이터
        res_data = {}

        if not (email and password and re_password):
            res_data['error']='모든 값을 입력하세요'
        # 비밀번호와 비밀번호 확인이 다르면 경고문자
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Users(
                email=email,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'users/register.html', res_data)

'''
class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = Users(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


