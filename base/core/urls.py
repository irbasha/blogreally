from django.urls import path
from .views import (
    home,
    detail,
    about,
    contact,
    success,
)

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
]
