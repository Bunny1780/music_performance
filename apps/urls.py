from django.urls import path, include
from . import views
app_name = "apps"

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.user_login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.user_logout, name="logout"),
    path('operation', views.operation, name="operation"),
    path('operation/<int:id>', views.edit, name="edit"),
    path('operation/<int:id>/delete', views.delete, name="delete"),
]
