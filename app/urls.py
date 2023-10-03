from django.urls import path

from app import views


urlpatterns = [
    path('categories/', views.CATEGORIES, name='categories'),
]