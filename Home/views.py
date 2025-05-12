from django.views import View
from django.shortcuts import render
from .models import UserRegistration
from .serializers import UserRegistrationSerializer
# Create your views here.

# @api_view(['GET'])
# def indexPage(request):
#     if request.method == 'GET':
#         users= UserRegistration.objects.all()
#         serializer = UserRegistrationSerializer(users, many=True)
#         return HttpResponse(serializer.data)
#     return render(request, 'index.html')

class IndexPageView(View):
    def get(self, request):
        users = UserRegistration.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return render(request, 'index.html', {'users': serializer.data})