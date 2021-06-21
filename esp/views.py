import rest_framework
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import RegisterUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import random
import time

# Create your views here.


def generate_expression():


    random.seed(int(time.time()))
    item_no = random.randint(10, 20)


    sol = random.randint(1, 1000)
    ex = str(sol)

    for i in range(item_no):
        num = random.randint(1, 1000)

        if random.randint(0, 1) % 2 == 0:
            sol += num
            ex += '+'
        else:
            sol -= num
            ex += '-'

        ex += str(num)
        
    return ex , sol

@api_view(['POST'])
def register(request):

    data = request.data

    s = RegisterUserSerializer(data=data)

    if s.is_valid():

        try:
            user = User.objects.get(chipID=data['chipID'])
            s.update(user, s.validated_data)
        except:
            user = s.save()

    else:
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

    token , created = Token.objects.get_or_create(user=user)

    if not created:
        token.delete()
        token = Token.objects.create(user=user)


    return Response(data={'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_expression(request):

    user = request.user
    user : User

    ex , sol = generate_expression()

    user.expression = ex
    user.solution = sol
    user.exp_timestamp = int(time.time()) + 1

    user.save()

    return Response(data={'expression':ex},status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_solution(request):
    
    user = request.user
    user : User


    now = int(time.time())

    if now - user.exp_timestamp > 5:
        return Response(data={'error':'time limit , you should sumbit your solution under 5 second. Please get a new expression and try again'},status=status.HTTP_400_BAD_REQUEST)

    try:
        sol = int(request.data['solution'])
    except:
        return Response(data={'error':'solution not found or presencted in wrong format.'},status=status.HTTP_400_BAD_REQUEST)


    if user.solution == sol:
        return Response(data={'result':'correct'},status=status.HTTP_200_OK)
    else:
        return Response(data={'result':'wrong'},status=status.HTTP_200_OK)