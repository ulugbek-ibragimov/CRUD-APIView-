from django.urls import path

from .serializers import ProfileSerializer
from .views import CategoryAPIView, api_root, TagAPIView, PostAPIView, CategoryDeleteAPIView, \
    ProfileListCreateAPIView, ProfileDetailUpdateDeleteAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<int:id>/', PostAPIView.as_view(), name='posts'),
    path('category/<int:id>/', CategoryAPIView.as_view(), name='category'),
    path('category/<int:id>/delete/', CategoryDeleteAPIView.as_view(), name='category'),
    path('category/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('profile/<int:id>/', ProfileDetailUpdateDeleteAPIView.as_view(), name='profiles'),
    path('profile/', ProfileListCreateAPIView.as_view(), name='profiles'),
    path('', api_root),
]