from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models.userModel import User
from app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class ListPostUserView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
