# formapi/urls.py
from django.urls import path
from .views import AddUser, GetUsers

urlpatterns = [
    path('formData/add-user/', AddUser.as_view()),
    path('formData/get-users/', GetUsers.as_view()),
]
