from django.urls import path

from .views import CreateBlogView, UpdateBlogView, BlogListView, BlogDeleteView

app_name = "blogs"

urlpatterns = [
    path("create/", CreateBlogView.as_view(), name="create"),
    path("update/<str:pk>/", UpdateBlogView.as_view(), name="update"),
    path("", BlogListView.as_view(), name="list"),
    path("delete/<str:pk>/", BlogDeleteView.as_view(), name="delete"),
]
