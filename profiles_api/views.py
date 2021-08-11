from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIview features"""

        an_apiview = [
            'Use HTTP methods as function (get,put,post,delete)',                
            'is similar traditional django view',
            'Gives you most control over application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message' : 'hello', 'an_apiview' : an_apiview})

    def post(self,request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method','PUT'})

    def delete(self,request,pk=None):
        """Handle deleting an object"""
        return Response({'method':'DELETE'})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    