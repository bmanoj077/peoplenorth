from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListView(APIView):
    def get(self, request):
        root_nodes = Employee.objects.filter(parent=None)  # Fetch only root nodes (e.g., "John")
        serializer = EmployeeSerializer(root_nodes, many=True)
        return Response(serializer.data)
