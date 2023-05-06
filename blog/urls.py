from django.urls import path
from blog.views import *

urlpatterns = [
    
    path('',home_blog,name="home_blog"),
    path('form_cad/',frm_cad_user,name='form_cad_user'),
    path('form_login/',frm_login,name='form_login'),
    path('page_post/',pg_post,name='page_post'),
    path('cad_usuario/',cad_user,name='cadastrar'),
    path('login/',realizar_login,name='login'),
]