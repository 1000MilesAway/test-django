from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ImageList.as_view(), name='image list'),
    path('add', views.add_image, name='add image'),
    path('^resize/(?P<image_id>\d+)/$', views.resize_image, name='resize image'),
]
