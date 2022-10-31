from rest_framework import serializers
from .models import Electronic, Category
from django.contrib.auth.models import User



class ElectronicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_superuser(username=validated_data.get('username'), password=validated_data.get('password'))
        print(validated_data)
        user.save()
        return User(**validated_data)