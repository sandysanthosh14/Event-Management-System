# serializers.py
from rest_framework import serializers
from .models import EventCategory,Event

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['name', 'code', 'image', 'priority', 'status']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
