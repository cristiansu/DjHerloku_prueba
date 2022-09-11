from django.urls import path, include
from .views import home, hello_reader

urlpatterns = [
    path('home/', home, name='home'),
    path('', hello_reader, name='logging'),
]