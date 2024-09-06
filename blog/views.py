from audioop import reverse
from logging import exception

from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id", None)  # id topilmasa None qiymat qabul qilinadi
        if not id:
            items = Category.objects.all()  # annotate(count=Count('posts')).all()
            serializer = CategorySerializer(items, many=True)
            return Response(serializer.data)
        item = Category.objects.get(id=id)
        serializer = CategorySerializer(item)
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

class CategoryDeleteAPIView(APIView):
    def delete(self, request, id):
        try :
            item = Category.objects.get(id=id)
        except:
            return Response({"error": "object not found"})
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id", None)  # id topilmasa None qiymat qabul qilinadi
        if not id:
            items = Post.objects.all() #annotate(count=Count('posts')).all()
            serializer = PostSerializer(items, many=True)
            return Response(serializer.data)
        item = Post.objects.get(id=id)
        serializer = PostSerializer(item)
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
    def delete(self, request, id):
        try :
            item = Post.objects.get(id=id)
        except:
            return Response({"error": "method delete is not allowed"})
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProfileListCreateAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




# category_new = Category.objects.create( # bu yerda ModelSerializer ning
#             title = request.data['title'],      # def create funk.ni override
#             order = request.data['order']       # qilyapmiz. Aslida shart emas
#         )                                       # def create ishlatilganda
#         return Response(CategorySerializer(category_new).data)
#     #     return Response(model_to_dict(category_new))
