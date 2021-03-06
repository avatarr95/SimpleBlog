from django.urls import path
from . import views

app_name = 'my_blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/<slug:post>/', views.post_detail_view, name="post_detail")
]
