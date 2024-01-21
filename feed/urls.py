from django.urls import path
from .views import HomePageView,PostDetailView,AddPostView

app_name ='feed'    #is gonna be used for namespace in the project\urls.py

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post')
]
