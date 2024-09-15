# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.employee_list, name='employee_list'),
#     path('add/', views.add_employee, name='add_employee'),
#     path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
#     path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
# ]



from django.urls import path
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]