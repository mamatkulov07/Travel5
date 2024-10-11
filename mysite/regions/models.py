from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)  # Имя
    last_name = models.CharField(max_length=30)   # Фамилия
    date_of_birth = models.DateField(null=True, blank=True)  # Дата рождения
    age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')


class HomePage(models.Model):
    name = models.CharField(max_length=100)
    image_map = models.ImageField(verbose_name="Изображение карты", upload_to='homepageimage/')
    description = models.TextField(verbose_name="Описание")
    earth = models.CharField(max_length=200, verbose_name='"от Бишкекка до Нарына"')


class Regions(models.Model):
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')


class Places(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание")
    description_comment = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    period = models.CHOISEC_Period = (
        ("January ", "January "),
        ("February", "February"),
        ("March", "March"),
        ("April", "April "),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November ", "November "),
        ("December", "December"),
    )
    star = models.CharField(max_length=16, choices=period)


class Hotels(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", upload_to='image/')
    description = models.TextField(verbose_name="Описание")
    image_map_hotel = models.ImageField(verbose_name="Изображение", upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    image_hotels = models.ImageField(verbose_name="Изображение", upload_to='image/')
    price = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=100)
    description_hotel = models.TextField(verbose_name="Описание")


class Kitchen(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    image_map_restaurants = models.ImageField(verbose_name="Изображение", upload_to='image/')
    stars_restaurants = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    description_restaurants = models.TextField(verbose_name="Описание")
    phone_number_restaurants = models.IntegerField(default=0)
    email_restaurants = models.EmailField(max_length=200)
    hotel = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class Event(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')
    date = models.DateField()
    video = models.FileField(upload_to='video/')
    places = models.ForeignKey(Places, on_delete=models.CASCADE)


class Attractions(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    image = models.ImageField(upload_to='image/')
    description_attractions = models.TextField(verbose_name="Описание")
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class Gallery(models.Model):
    image_map = models.ImageField(upload_to='image/')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    descriptions = models.TextField()


class Culture(models.Model):
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='image/')
    hotel = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class CultureGames(models.Model):
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='image/')
    hotel = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class CultureNationalClothes(models.Model):
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')


class CultureHandCrafts(models.Model):
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')


class CultureCurrency(models.Model):
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')


class CultureKitchen(models.Model):
    description = models.TextField(verbose_name="Описание")
    image_kitchen = models.ImageField(upload_to='image/')
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class CultureNationalInstruments(models.Model):
    description = models.TextField(verbose_name="Описание")
    image_event = models.ImageField(upload_to='image/')
    hotel = models.ForeignKey(HomePage, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)


class Review(models.Model):
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    places = models.ForeignKey(Places, on_delete=models.CASCADE, null=True, blank=True)
    hotels = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True, blank=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    attractions = models.ForeignKey(Attractions, on_delete=models.CASCADE, null=True, blank=True)
    parent_review = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

