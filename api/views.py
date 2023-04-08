from rest_framework import generics
from rest_framework.response import Response # import Response module
from rest_framework import status # import status module
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = self.serializer_class(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        residential_address_data = request.data.pop('residential_address', None)
        if residential_address_data:
            residential_address_serializer = ResidentialAddressSerializer(data=residential_address_data)
            residential_address_serializer.is_valid(raise_exception=True)
            residential_address = residential_address_serializer.save()
            user.residential_address = residential_address
            user.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED) # use Response module

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user_serializer = self.serializer_class(user, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        residential_address_data = request.data.pop('residential_address', None)
        if residential_address_data:
            if user.residential_address:
                residential_address_serializer = ResidentialAddressSerializer(user.residential_address, data=residential_address_data, partial=True)
            else:
                residential_address_serializer = ResidentialAddressSerializer(data=residential_address_data)
            residential_address_serializer.is_valid(raise_exception=True)
            residential_address = residential_address_serializer.save()
            user.residential_address = residential_address
            user.save()
        return Response(user_serializer.data, status=status.HTTP_200_OK) # use Response module





  






