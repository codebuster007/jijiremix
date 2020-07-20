from rest_framework import serializers
from store.serializers import ItemSerialiazer
from .models import ORMUser

class UserSerializer(serializers.ModelSerializer):
    items = ItemSerialiazer(source='owner',
                            many=True, required=False)
    class Meta:
        model = ORMUser
        fields = ('user_id', 'email', 'first_name', 'last_name', 'residence_state', 'items',)