from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework import status


@api_view(['GET'])
def get_data(request):
    try:
        users = User.objects.all()
    except User.DoesNotExist:
        return Response({'message': 'No users found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request, pk):
    try:
        users = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'message': 'User not found! '}, status=status.HTTP_404_NOT_FOUND)    
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'message':'User not found! '}, status=status.HTTP_404_NOT_FOUND)    
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteUser(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'message':'User not found!'},status=status.HTTP_404_NOT_FOUND)    
    user.delete()
    return Response('User successfully deleted!')

def add_numbers(a,b):
    return a + b

result = add_numbers(2,3)
print(result)