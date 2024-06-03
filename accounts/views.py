from django.forms import BaseModelForm, ModelForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.generic import CreateView, FormView

from .models import User


class SignupView(CreateView):
    model = User
    fields = "__all__"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return HttpResponse(f"User {user.username} created successfully.")


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]

    def is_valid(self) -> bool:
        objs = User.objects.filter(username=self.data.get("username", None))

        if objs.exists() and objs.count() == 1:
            self.instance = objs.first()
            return True
        self.errors.setdefault("username", ["User does not exist."])
        return False


class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.instance
        login(self.request, user)
        return HttpResponse(f"User {user.username} logged in successfully.")
