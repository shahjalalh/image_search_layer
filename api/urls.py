from django.conf.urls import url, include
from .views import ImageListAPIView, ImageSearchListAPIView

urlpatterns = [
    url(r'^imagesearch/(?P<term>[a-zA-Z0-9]+)', ImageListAPIView.as_view()),
    url(r'^latest/imagesearch', ImageSearchListAPIView.as_view()),
]
