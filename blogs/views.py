from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .models import Blog


class CreateBlogView(CreateView):
    model = Blog
    fields = "__all__"
    success_url = "/blogs/"


class UpdateBlogView(UpdateView):
    model = Blog
    fields = "__all__"
    success_url = "/blogs/"
    template_name_suffix = "_update_form"


class BlogListView(ListView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = "/blogs/"
