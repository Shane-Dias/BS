from rest_framework import serializers
from .models import Incidents, User, Comment
import json

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = '__all__'

    def validate_location(self, value):
        if isinstance(value, str):
            try:
                value = json.loads(value)  # Convert JSON string to dictionary
            except json.JSONDecodeError:
                raise serializers.ValidationError("Invalid location data")
        if not isinstance(value, dict) or 'latitude' not in value or 'longitude' not in value:
            raise serializers.ValidationError("Invalid location data")
        return value

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             phone_number=validated_data['phone_number'],
#             aadhar_number=validated_data['aadhar_number'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             address=validated_data['address'],
#             emergency_contact1=validated_data['emergency_contact1'],
#             emergency_contact2=validated_data['emergency_contact2']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'commented_by', 'commented_at', 'useful', 'commented_on']
        read_only_fields = ['commented_by', 'commented_at']

    def validate(self, attrs):
        attrs.pop('user_email', None)  # Remove if present
        return attrs

class IncidentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Nested comments
    reported_by = UserSerializer(read_only=True)  # Include reporter details
    
    class Meta:
        model = Incidents
        fields = '__all__'
        read_only_fields = ['reported_at', 'status', 'remarks', 'true_or_false']
