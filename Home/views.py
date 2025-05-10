from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.models import UserRegistration
from Home.serializers import UserRegistrationSerializer
# Create your views here.

@api_view(['GET'])
def indexPage(request):
    if request.method == 'GET':
        users= UserRegistration.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        JsonResponse(serializer.data, safe=False)