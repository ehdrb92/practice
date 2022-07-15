from django.urls import path

from models import User

urlpatterns = [
    path('/signin', User.as_View())    
]
