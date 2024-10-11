from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import HomePageFilter
from rest_framework import viewsets, status, generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer
import random
import string
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Создаем профайл пользователя
        profile_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'date_of_birth': request.data.get('date_of_birth'),
            'age': request.data.get('age'),
            'phone_number': request.data.get('phone_number'),
            'user': user
        }
        profile_serializer = UserProfileSerializer(data=profile_data)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer  # Добавляем пустой сериализатор

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def send_test_email(request):
    send_mail(
        'Тема письма',
        'Это текстовое сообщение.',
        'usmanmamatkulov8@gmail.com ',  # Замените на ваш email
        ['usmanmamatkulov36@gmail.com'],         # Замените на email получателя
        fail_silently=False,
    )
    return HttpResponse("Письмо отправлено!")


def generate_code(length=6):
    """Генерирует случайный код указанной длины."""
    characters = string.digits  # Используем только цифры
    return ''.join(random.choice(characters) for _ in range(length))


def send_email(request):
    # Генерируем уникальный код
    code = generate_code()

    # Создайте HTML-контент
    html_content = render_to_string('email_template.html', {'code': code})

    # Настройка письма
    email = EmailMessage(
        '7777',
        html_content,
        'usmanmamatkulov8@gmail.com',  # Ваш email
        ['usmanmamatkulov36@gmail.com'],  # Email получателя
    )
    email.content_subtype = "html"  # Установите тип контента на HTML

    # Отправка письма
    email.send()

    return HttpResponse('Письмо с кодом отправлено!')


class HomePageViewSets(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = HomePageFilter
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegionsViewSets(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlacesViewSets(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HotelsViewSets(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KitchenViewSets(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventViewSets(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AttractionsView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GalleryViewSets(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureViewSets(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureGamesViewSets(viewsets.ModelViewSet):
    queryset = CultureGames.objects.all()
    serializer_class = CultureGamesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureNationalClothesViewSets(viewsets.ModelViewSet):
    queryset = CultureNationalClothes.objects.all()
    serializer_class = CultureNationalClothesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureHandCraftsViewSets(viewsets.ModelViewSet):
    queryset = CultureHandCrafts.objects.all()
    serializer_class = CultureHandCraftsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureCurrencyViewSets(viewsets.ModelViewSet):
    queryset = CultureCurrency.objects.all()
    serializer_class = CultureCurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureKitchenViewSets(viewsets.ModelViewSet):
    queryset = CultureKitchen.objects.all()
    serializer_class = CultureKitchenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CultureNationalInstrumentsViewSets(viewsets.ModelViewSet):
    queryset = CultureNationalInstruments.objects.all()
    serializer_class = CultureNationalInstrumentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FavoriteViewSets(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['region']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [SearchFilter]
    search_fields = ['text']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





