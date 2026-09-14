from django.http import request
from django.shortcuts import render
from .models import User
from users.forms import ProfileForm
from users.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

@api_view(["GET", "POST"])
def register_user(request):

    if request.method == "GET":
        users = User.objects.all()
        serializer = Serializer(users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    serializer = Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "id": request.user.id,
            "fullname": request.user.full_name,
            "email": request.user.email,
            })

    