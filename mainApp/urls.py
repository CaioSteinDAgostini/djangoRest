from django.urls import include, path
from rest_framework import routers
 
from .views import *
 
router = routers.DefaultRouter()
""" router.register(r'domains', DomainsViewSet) """
 
urlpatterns = [
    path('', include(router.urls)),
    path('documents', views.documents),
    path('documents/<int:id>', views.documentsById),
    path('api-auth/', include('rest_framework.urls'))
]