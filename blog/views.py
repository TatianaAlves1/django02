from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from blog.models import Post

# Create your views here.
def home_blog(request):
    posts = Post.objects.all().order_by('-dt_post')[:5]
    dic = {'dados':posts}
    return render(request,'blog/index.html',dic)

def frm_cad_user(request):
    return render(request,'blog/formCadUser.html')

def frm_login(request):
    return render(request,'blog/formlogin.html')

def pg_post(request):
    return render(request,'blog/post.html')

def cad_user(request):
    try:
        nome  = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(nome,email,senha)
        if User.objects.filter(username = nome):
            print("usuario cadastrado")
            return redirect(frm_login)
        else:
            user = User.objects.create_user(nome,email,senha)
            print("cadastrado!")
            return redirect(home_blog)
    except Exception as e:
        print(e)
        print("Não realizou o cadastro!")
        return redirect(home_blog)

def realizar_login(request):
        nome  = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = auth.authenticate(request,username=nome,password=senha)
        if user  is not None:
            print('entrou...')
            auth.login(request,user)
            print('login ok')
            return redirect(home_blog)
            messages.success(request,'Login com Sucesso!!!')
        else:
            messages.error(request,'dados inválidos')
            return redirect(frm_login)
        