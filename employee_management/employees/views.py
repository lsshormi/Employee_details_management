from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        date_of_birth = self.request.GET.get('date_of_birth')
        email = self.request.GET.get('email')
        mobile = self.request.GET.get('mobile')
        sort_by = self.request.GET.get('sort_by', 'first_name')
        sort_order = self.request.GET.get('sort_order', 'asc')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query)
            )
        if date_of_birth:
            queryset = queryset.filter(date_of_birth=date_of_birth)
        if email:
            queryset = queryset.filter(email__icontains=email)
        if mobile:
            queryset = queryset.filter(mobile__icontains=mobile)

        if sort_order == 'desc':
            sort_by = f'-{sort_by}'

        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by', 'first_name')
        context['sort_order'] = self.request.GET.get('sort_order', 'asc')
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/delete_employee.html'
    success_url = reverse_lazy('employee_list')