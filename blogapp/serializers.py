from rest_framework import serializers
from .models import Post, employee
from django.contrib.auth.models import User
from rest_framework import permissions

class Postserializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')



class Employeesserializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=employee
        fields=('First_name', 'Last_name', 'profile_pic', 'emp_id', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=employee.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'employees')
