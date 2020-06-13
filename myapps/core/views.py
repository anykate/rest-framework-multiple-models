from django.shortcuts import render, redirect
from django.views import View
from .models import Employee, Sport
from .serializers import EmployeeSerializer, SportSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests


# Create your views here.
@api_view(['GET'])
def api_showmultiplemodels(request):
    emp_obj = Employee.objects.all()
    sport_obj = Sport.objects.all()
    emp_serialized_obj = EmployeeSerializer(emp_obj, many=True)
    sport_serialized_obj = SportSerializer(sport_obj, many=True)
    result_serialized_obj = emp_serialized_obj.data+sport_serialized_obj.data
    return Response(result_serialized_obj, status=status.HTTP_200_OK)


def showmultiplemodels(request):
    data = requests.get('http://localhost:8000/api/showmultiplemodels/')
    result = data.json()
    return render(request, 'core/show.html', {'emp_data': result, 'sport_data': result})
