from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from snippets import serializers

#API'mizin kökü, mevcut tüm snippet'lerin listelenmesini veya yeni bir snippet oluşturulmasını destekleyen bir görünüm olacaktır.


# @csrf_exempt
# def snippet_list(request):
    
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#CSRF belirtecine sahip olmayacak istemcilerden bu görünüme POST yapabilmek istediğimiz için, görünümü csrf_exempt olarak işaretlememiz gerektiğini unutmayın.


#Ayrıca, tek bir snippet'e karşılık gelen ve snippet'i almak, güncellemek veya silmek için kullanılabilecek bir görünüme ihtiyacımız olacak

# @csrf_exempt
# def snippet_detail(request, pk):
    
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
    
#request.POST  # Only handles form data.  Only works for 'POST' method.
#request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', 'DELETE'])
def snippet_detail(request, pk, format=None):
    
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Yanıtlarımızın artık tek bir içerik türüne bağlı olmadığı gerçeğinden yararlanmak için, API uç noktalarımıza biçim son ekleri için destek ekleyelim.
#Biçim son eklerini kullanmak bize belirli bir biçime açıkça atıfta bulunan URL'ler verir ve API'mizin http://example.com/api/items/4.json gibi URL'leri işleyebileceği anlamına gelir.
#Her iki görünüme de bir format anahtar kelime argümanı ekleyerek başlayalım.
#Şimdi, mevcut URL'lere ek olarak bir dizi format_suffix_patterns eklemek için snippet'leri/urls.py dosyasını biraz güncelleyin.