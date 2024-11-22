from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.create_album, name='create_album'),
    path('list/', views.SocialList.as_view()),
    path('photo/', views.PhotoList.as_view()),
]
