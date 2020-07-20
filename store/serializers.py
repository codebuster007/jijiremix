import os

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from accounts.models import ORMUser
from .models import ORMItem, ORMBuyer


class BuyerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ORMBuyer
        fields = '__all__'
    
    def save(self):
        item = self.context.get("item")
        print('##### ', item)
        # if re

        return super(BuyerSerializer, self).save()


class BuyerListing(serializers.RelatedField):
    
    def to_representation(self, value):
        return {
            'buyer_id': value.id,
            'name': value.name,
            'email': value.email,
            'location': value.location
        }
    
    def to_internal_value(self, data):
        if data is None:
            raise serializers.ValidationError(_('Invalid Id'))
        return ORMBuyer.objects.get(id=int(data))

class ItemOwnerListing(serializers.RelatedField):
    
    def to_representation(self, value):
        return {
            'owner_id': value.user_id,
            'first_name': value.first_name,
            'last_name': value.last_name,
            'residence_state': value.residence_state
        }
    
    def to_internal_value(self, data):
        if data is None:
            raise serializers.ValidationError(_('Invalid Id'))
        return ORMUser.objects.get(user_id=data)

class ItemSerialiazer(serializers.ModelSerializer):
    sold_to = BuyerListing(queryset=ORMBuyer.objects.all())
    owner = ItemOwnerListing(queryset=ORMUser.objects.all())
    
    intrested_buyers = BuyerSerializer(source='item',
                                       many=True, required=False)
    class Meta:
        model = ORMItem
        fields = '__all__'


    def update(self, instance, validated_data):

        if instance.is_sold is not None:
            instance.is_sold = validated_data.get('is_sold', instance.is_sold)

        # The initial value of sold to is None
        # This is gauranteed to execute one
        if instance.sold_to is None:
            instance.sold_to = validated_data.get('sold_to', instance.sold_to)

        # Incase seller sells to some other buyer
        if instance.sold_to is not None:
            instance.sold_to = validated_data.get('sold_to', instance.sold_to)
        
        if instance.name is not None:
            instance.name = validated_data.get('name', instance.name)
        
        if instance.description is not None:
            instance.description = validated_data.get('description', instance.description)
        
        if instance.price is not None:
            instance.price = validated_data.get('price', instance.price)
        
        try:
            if instance.image is not None and \
                validated_data.get('image', None) is not None:
                os.remove(instance.image.file.name)
        except FileNotFoundError:
            pass
        finally:
            instance.image = validated_data.get('image', instance.image)
        
        instance.save()

        return instance
    
    def save(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            self.validated_data['owner'] = user
        return super().save()

