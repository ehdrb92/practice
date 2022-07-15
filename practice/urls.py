from django.urls import path, include

urlpatterns = [
    path('practice', include('app1.urls'))
]
