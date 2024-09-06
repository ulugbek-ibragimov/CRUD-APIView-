from audioop import reverse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import PostSerializer, CategorySerializer, TagSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "posts":reverse("posts", request=request, format=format),
            "categories":reverse("categories", request=request, format=format),
            "tags":reverse("tags", request=request, format=format),
            "profiles":reverse("profiles", request=request, format=format),
        }
    )



class CategoryAPIView(APIView):
    def get(self, request):
        items = Category.objects.all()  #annotate(count=Count('posts')).all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwarg):
        id = kwarg.get("id", None) #id topilmasa None qiymat qabul qilinadi
        if not id:
            return Response({"error":"method put is not allowed"})
        try:
            instance = Category.objects.get(id=id)
        except:
            return Response({"error": "method put is not allowed"})
        serializer = CategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save() #bu yerdan serializersdagi def updete chaqiriladi
        return Response(serializer.data)

class PostAPIView(APIView):
    def get(self, request):
        items = Post.objects.all() #annotate(count=Count('posts')).all()
        serializer = PostSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwarg):
        id = kwarg.get("id", None) #id topilmasa None qiymat qabul qilinadi
        if not id:
            return Response({"error":"method put is not allowed"})
        try:
            instance = Post.objects.get(id=id)
        except:
            return Response({"error": "method put is not allowed"})
        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save() #bu yerdan serializersdagi def updete chaqiriladi
        return Response(serializer.data)

class TagAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProfileAPIView(APIView):
    def get(self, request):
        items = Profile.objects.all() #annotate(count=Count('posts')).all()
        serializer = ProfileSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwarg):
        id = kwarg.get("id", None) #id topilmasa None qiymat qabul qilinadi
        if not id:
            return Response({"error":"method put is not allowed"})
        try:
            instance = Profile.objects.get(id=id)
        except:
            return Response({"error": "method put is not allowed"})
        serializer = ProfileSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save() #bu yerdan serializersdagi def updete chaqiriladi
        return Response(serializer.data)







# category_new = Category.objects.create( # bu yerda ModelSerializer ning
#             title = request.data['title'],      # def create funk.ni override
#             order = request.data['order']       # qilyapmiz. Aslida shart emas
#         )                                       # def create ishlatilganda
#         return Response(CategorySerializer(category_new).data)
#     #     return Response(model_to_dict(category_new))
