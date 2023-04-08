from rest_framework import serializers
from .models import User, ResidentialAddress

class ResidentialAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialAddress
        fields = ['id', 'address_name', 'state', 'city', 'zip_code']

class UserSerializer(serializers.ModelSerializer):
    residential_addresses = ResidentialAddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone_number', 'email_address', 'avatar_url', 'description', 
                  'date_of_birth', 'gender', 'occupation', 'experience', 'postal_code', 'residential_addresses']

    def create(self, validated_data):
        residential_addresses_data = validated_data.pop('residential_addresses')
        user = User.objects.create(**validated_data)
        for residential_address_data in residential_addresses_data:
            ResidentialAddress.objects.create(user=user, **residential_address_data)
        return user

    def update(self, instance, validated_data):
        residential_addresses_data = validated_data.pop('residential_addresses')
        residential_addresses = (instance.residential_addresses).all()
        residential_addresses = list(residential_addresses)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.avatar_url = validated_data.get('avatar_url', instance.avatar_url)
        instance.description = validated_data.get('description', instance.description)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()

        for residential_address_data in residential_addresses_data:
            residential_address = residential_addresses.pop(0)
            residential_address.address_name = residential_address_data.get('address_name', residential_address.address_name)
            residential_address.state = residential_address_data.get('state', residential_address.state)
            residential_address.city = residential_address_data.get('city', residential_address.city)
            residential_address.zip_code = residential_address_data.get('zip_code', residential_address.zip_code)
            residential_address.save()
        return instance















