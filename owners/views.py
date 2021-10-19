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

    def get(self, request):
        owners = Owner.objects.all()       

        result = []

        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []

            for dog in dogs:
                
                dog_list.append(
                    {
                        "name" : dog.name,
                        "age" : dog.age
                    }
                )

            result.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age": owner.age,
                    "dog_list" : dog_list
                }
            )
                
        return JsonResponse({"result" : result}, status = 200)

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

    def get(self, request):

        dogs = Dog.objects.all()

        result = []
        for dog in dogs:
            result.append(
                {
                    "id" : dog.id,
                    "name" : dog.name,
                    "age": dog.age,
                    "owner" : {
                        "id" : dog.owner.id,
                        "name" : dog.owner.name,
                        "email" : dog.owner.email,
                        "age" : dog.owner.age

                    }

                }
            )

            return JsonResponse({"dogs" : result}, status = 200)