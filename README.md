This is a simple project to provide a basic set of entities mapped to a relational DB, and to provide a basic REST API.

It has no access control, no pagination, and it does not have endpoints for all of the entities. If you want to see how it could be if I had done it all, take a look at this (Java+Spring boot project)[https://github.com/CaioSteinDAgostini/fabula].

## What it covers

 - creating a Django App
 - managing dependencies
 - model serializers
 - embedded models/objects (objects that reference other objects)
 - publishing routes with Http Methods (GET, PUT, PATCH, DELETE) and proper handling of HTTP response codes:
   ```python
@api_view(['GET', 'POST'])
def documents(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True, context={'request':request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def documentsById(request, id):
    try:
        document = Document.objects.get(pk=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print("GET GET GET")
        serializer = DocumentSerializer(document, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = DocumentSerializer(instance=document, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = DocumentSerializer(instance=document, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   ``` 
