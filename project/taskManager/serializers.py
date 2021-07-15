from rest_framework import serializers
from .models import Project 
from django.contrib.auth.models import User

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'id', 'projectName', 'DateOfStart','projectSize'] 

