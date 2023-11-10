from django.shortcuts import render
from django.views import View

from .forms import UserRegistrationForm


class SignupView(View):
    form_class = UserRegistrationForm
    template_name = 'users/signup.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass