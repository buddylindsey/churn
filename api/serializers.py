from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'title', 'slug', 'description', 'created', 'completion_date',
            'due_date', 'order', 'category')
