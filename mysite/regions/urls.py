from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('send-email/', send_test_email, name='send_email'),


    path('homepage/', HomePageViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='homepage_list'),

    path('homepage/<int:pk>/', HomePageViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='homepage_detail'),

    path('regions/', RegionsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='regions_list'),

    path('regions/<int:pk>/', RegionsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='regions_detail'),


    path('places/', PlacesViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='places_list'),

    path('places/<int:pk>/', PlacesViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='places_detail'),


    path('hotels', HotelsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='hotels_list'),

    path('hotels/<int:pk>/', HotelsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotels_detail'),


    path('kitchen', KitchenViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='kitchen_list'),

    path('kitchen/<int:pk>/', KitchenViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='kitchen_detail'),


    path('event', EventViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='event_list'),

    path('event/<int:pk>/', EventViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='event_detail'),

    path('attractions/', AttractionsView.as_view({'get': 'list', 'post': 'create'}), name='attractions_list'),

    path('attractions/<int:pk>/', AttractionsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='attractions_detail'),


    path('gallery', GalleryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='gallery_list'),

    path('gallery/<int:pk>/', GalleryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='gallery_detail'),


    path('culture', CultureViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culture_list'),

    path('culture/<int:pk>/', CultureViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culture_detail'),


    path('culturegames', CultureGamesViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturegames_list'),

    path('culturegames/<int:pk>/', CultureGamesViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturegames_detail'),


    path('culturenationalclothes', CultureNationalClothesViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturenationalclothes_list'),

    path('culturenationalclothes/<int:pk>/', CultureNationalClothesViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturenationalclothes_detail'),


    path('culturehandcrafts', CultureHandCraftsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturehandcrafts_list'),

    path('culturehandcrafts/<int:pk>/', CultureHandCraftsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturehandcrafts_detail'),


    path('culturecurrency', CultureCurrencyViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturecurrency_list'),

    path('culturecurrency/<int:pk>/', CultureCurrencyViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturecurrency_detail'),


    path('culturekitchen', CultureKitchenViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturekitchen_list'),

    path('culturekitchen/<int:pk>/', CultureKitchenViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturekitchen_detail'),


    path('culturenationalinstruments', CultureNationalInstrumentsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='culturenationalinstruments_list'),

    path('culturenationalinstruments/<int:pk>/', CultureNationalInstrumentsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='culturenationalinstruments_detail'),


    path('favorite', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_list'),

    path('favorite/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),


    path('review', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),

    path('review/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),


]



