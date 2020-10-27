from django.urls import path

import authnapp.views as authnapp

from .apps import AuthnappConfig

app_name = AuthnappConfig.name #"authnapp"

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
    path("register/", authnapp.register, name="register"),
    path("edit/", authnapp.edit, name="edit"),
]
