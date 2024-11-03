from django.urls import path
from Apps.usuario.views import login_view,logout_view

app_name='usuario'

urlpatterns = [
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout')
    

]