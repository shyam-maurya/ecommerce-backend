from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, data):
        return User.objects.create_user(**data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','is_customer','is_admin_user')
        read_only_fields = fields
