from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = "Home"),
    path('login/',views.login,name = "Login"),
    path('regsiter/',views.regsiter,name = "Register"),
]
