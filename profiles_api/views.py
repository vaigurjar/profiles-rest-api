from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self,request,format=None):
        """Returns a list of APIview features"""

        an_apiview = [
            'Use HTTP methods as function (get,put,post,delete)',                
            'is similar traditional django view',
            'Gives you most control over application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message' : 'hello', 'an_apiview' : an_apiview})
