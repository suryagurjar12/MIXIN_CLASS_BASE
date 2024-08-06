from rest_framework import serializers
from .models import Snippet


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'name', 'email', 'city', 'rollno']