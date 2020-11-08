from django.urls import path
from .views import HomePageView,HomeDetailView,HomeCreateView,HomeUpdateView,HomeDeleteView


urlpatterns = [
    path('post/<int:pk>/delete/',HomeDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',HomeUpdateView.as_view(), name='post_edit'),
    path('post/new/', HomeCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', HomeDetailView.as_view(), name='post_detail'),
    path('',HomePageView.as_view(), name='home')

]