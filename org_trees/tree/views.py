from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import RetrieveAPIView

# Existing EmployeeListView (GET method)
class EmployeeListView(APIView):
    def get(self, request):
        root_nodes = Employee.objects.filter(parent=None)  # Fetch only root nodes (e.g., "John")
        serializer = EmployeeSerializer(root_nodes, many=True)
        return Response(serializer.data)
    
class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
# New EmployeeCreateView (POST method for creating employees)
class EmployeeCreateView(APIView):
    def post(self, request):
        # Deserialize the incoming data
        serializer = EmployeeSerializer(data=request.data)
        
        # Validate and save if valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeUpdateView(APIView):
    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDeleteView(APIView):
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)