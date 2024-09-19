from django.urls import path
from . import views

urlpatterns=[
    path("welcome", views.welcome, name='welcome'),
    path("", views.start, name='start'),
    path("login/", views.login, name='login'),
    path("registration/", views.registration, name='registration'),
    path("home/", views.home, name='home'),
    path("delete/<int:pk>/", views.delete_info, name='delete'),
    path("details_page/", views.details, name='details_page'),
    path("details/<int:pk>/", views.details, name="details"),
    path("update/", views.update_page, name="update_page"),
    path("delete/", views.delete_page, name="delete_page"),
    path("form/", views.form, name='form'),
    path("update/<int:pk>/", views.update, name="update"),
]
