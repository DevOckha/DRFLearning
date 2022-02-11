from operator import iconcat
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Bir yönlendirici oluşturun ve onunla görünüm kümelerimizi kaydedin.
router = DefaultRouter()
router.register(r'snippets', viewset=views.SnippetViewSet)
router.register(r'users', viewset=views.UserViewSet)


# API URL'leri artık yönlendirici tarafından otomatik olarak belirlenir.
urlpatterns = [
    path('', include(router.urls)),
]


"""Kullandığımız DefaultRouter sınıfı da bizim için API kök görünümünü otomatik olarak oluşturur, böylece artık api_root yöntemini görünüm modülümüzden silebiliriz."""






# urlpatterns = [
    
#     path('', views.api_root),
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#Bu ekstra url kalıplarını mutlaka eklememiz gerekmiyor, ancak bize belirli bir formata atıfta bulunmanın basit ve temiz bir yolunu sunuyor.


# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })