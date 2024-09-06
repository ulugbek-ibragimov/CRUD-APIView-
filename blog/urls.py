from django.urls import path

from .serializers import ProfileSerializer
from .views import CategoryAPIView, api_root, TagAPIView, PostAPIView, ProfileAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('posts/<int:id>/', PostAPIView.as_view(), name='posts'),
    path('category/', CategoryAPIView.as_view(), name='categories'),
    path('category/<int:id>/', CategoryAPIView.as_view(), name='category'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('profile/', ProfileAPIView.as_view(), name='profiles'),
    path('', api_root),
]