
# chat/views.py
from rest_framework import viewsets
from .models import User, Room, Message
from .serializers import UserSerializer, RoomSerializer, MessageSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout


# @api_view(['GET'])
# def current_user(request):
#     if request.user.is_authenticated:
#         return Response({
#             'id': request.user.id,
#             'username': request.user.username,
#             'email': request.user.email,
#         })
#     return Response({'error': 'Chưa đăng nhập'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Đăng xuất thành công'})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    # avatar = request.data.get('avatar')

    if not username or not email:
        return Response({'error': 'Thiếu thông tin username hoặc email'}, status=400)

    user = User.objects.filter(email=email).first()

    if user:
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            # 'avatar': user.avatar if user.avatar else None
        })
    else:
        try:
            new_user = User.objects.create_user(username=username, email=email,  password=None)
            return Response({
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                # 'avatar': new_user.avatar if new_user.avatar else None
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        ids = self.request.query_params.get('ids')
        if ids:
            ids_list = ids.split(',')
            return User.objects.filter(id__in=ids_list)
        return self.queryset


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get_queryset(self):
        room_id = self.request.query_params.get('roomId')
        if room_id:
            return Message.objects.filter(room_id=room_id)
        return self.queryset
