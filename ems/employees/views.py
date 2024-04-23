from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/login/'  # Redirect to login page after successful signup

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
