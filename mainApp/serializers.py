from rest_framework import serializers
 
from .models import Domain, Document
 
class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ('id','name')




class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'title', 'subtitle', 'domain')


