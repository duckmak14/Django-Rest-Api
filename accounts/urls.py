from . import views
from django.urls import path

urlpatterns=[
    path("signup", view=views.SignUpView.as_view(),name="signup"),
    path("login", view=views.LoginView.as_view(),name="login"),
]
