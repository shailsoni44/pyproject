from rest_framework import serializers
from .models import Register, Signup, Session

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"
        
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
