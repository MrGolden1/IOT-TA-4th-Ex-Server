from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    chipID = serializers.IntegerField()
    studentID = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['first_name','last_name','chipID','studentID']

    # def validate_studentID(self,value):
    #     pass
