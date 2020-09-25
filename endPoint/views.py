from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from endPoint.models import Employee
from django.core import serializers


def create(request):
    data = request.POST
    try:
        employee = Employee(eid=data['eid'],
                            ename=data['ename'],
                            eemail=data['eemail'],
                            econtact=data['econtact'])
        employee.save()
        return JsonResponse({'Created': 'New Record has been added'})
    except:
        return JsonResponse({'error': 'Not valid data'})


def index(request):
    try:
        employees = serializers.serialize("json", Employee.objects.all())
        return HttpResponse(employees)
    except ObjectDoesNotExist as err:
        return HttpResponse(err)


def employee(request, id):
    try:
        employee = Employee.objects.filter(id=id)
        employee = serializers.serialize("json", employee)
        return HttpResponse(employee)
    except ObjectDoesNotExist as err:
        return HttpResponse(err)


def update(request, id):
    try:
        employee = Employee.objects.get(id=id)
        data = request.POST
        employee.update_or_create(data)
        return JsonResponse({'Updated': ' Record has been updated'})
    except ObjectDoesNotExist as err:
        return HttpResponse(err)


def delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse({'response': 'Deleted'})
    except ObjectDoesNotExist as err:
        return HttpResponse(err)
