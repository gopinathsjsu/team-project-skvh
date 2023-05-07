from rest_framework.serializers import ModelSerializer
from Business.models import Plan, Class, Instructor
from rest_framework import serializers


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'