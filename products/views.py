import json

from django.views import View

from django.http import HttpResponse, JsonResponse
# Create your views here.

from .models import Product

class ProductListView(View) :
    def get(self, request) :

        products= Product.objects.all()

        result=[]

        for product in products:
            result.append(
                {
                    "id" : product.id,
                    "korean_name" : product.korean_name,
                    "english_name" : product.english_name,
                    "Category" : {
                        "id" : product.category.id,
                        "name" : product.category.name
                    }

                }
            )
        #client 요청을 처리할 수 있는 Logic
        return JsonResponse({"Products" : result}, status = 200)

    def post(self, request) :
        
        
        print(f"request.body :: {request.body}")
        input_data = json.loads(request.body)
        
        #Category.objects.create()

        Product.objects.create(
            korean_name = input_data["korean_name"],
            english_name = input_data["english_name"],
            description = input_data["description"],
            category_id = input_data["category_id"]
            )
        
        return JsonResponse({"message" : "SUCCESS"}, status=201)
