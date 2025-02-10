from django.urls import path
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,EmployeeDetailView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]

