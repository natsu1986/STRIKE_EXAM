from rest_framework import serializers
from strikeTaskWeb.models import task

class taskSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    pending_status = serializers.ReadOnlyField()

    class Meta:
        model = task
        fields = ['id', 'created', 'title', 'description', 'datetobecomplete', 'datecompleted', 'urgent', 'important', 'pending_status']    
        
class taskCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = task
        fields = ['id']
        read_only_fields = ['created', 'title', 'description', 'datecompleted', 'urgent', 'important', 'pending_status']    
