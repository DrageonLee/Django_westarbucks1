import json

from django.views import View

from django.http import HttpResponse, JsonResponse
# Create your views here.

from owners.models import Owner, Dog

class OwnerListView(View) :
    def post(self, request):

        print(f"request.body :: {request.body}")
        input_data = json.loads(request.body)

        Owner.objects.create(
            name = input_data["name"],
            email = input_data["email"],
            age = input_data["age"]
            )

        return JsonResponse({"message" : "SUCCESS"}, status = 201)

class DogListView(View) :
    def post(self, request):

        print(f"request.body :: {request.body}")
        input_data = json.loads(request.body)

        Dog.objects.create(
            name=input_data["name"],
            age=input_data["age"],
            owner_id=input_data["owner_id"]
            )

        
        return JsonResponse({"message" : "SUCCESS"}, status = 201)