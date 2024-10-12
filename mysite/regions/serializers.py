from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['age', 'phone_number', 'user']  # Указываем только поля для профиля

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class CultureGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureGames
        fields = '__all__'


class CultureNationalClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureNationalClothes
        fields = '__all__'


class CultureHandCraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureHandCrafts
        fields = '__all__'


class CultureCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureCurrency
        fields = '__all__'


class CultureKitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureKitchen
        fields = '__all__'


class CultureNationalInstrumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureNationalInstruments
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
