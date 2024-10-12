from .models import (HomePage, Regions, Hotels, Kitchen,
                     Places, Attractions, Review, CultureKitchen,
                     Culture, CultureCurrency, CultureGames, CultureNationalInstruments,
                     CultureNationalClothes, CultureHandCrafts, Gallery, Event)
from modeltranslation.translator import TranslationOptions, register


# @register(UserProfile)
# class ProductTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')


@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'earth',)


@register(Regions)
class RegionsTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Places)
class PlacesTranslationOptions(TranslationOptions):
    fields = ('description', 'description_comment',)


@register(Hotels)
class HotelsTranslationOptions(TranslationOptions):
    fields = ('description', 'description_hotel',)


@register(Kitchen)
class KitchenTranslationOptions(TranslationOptions):
    fields = ('description', 'description_restaurants',)


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Attractions)
class AttractionsTranslationOptions(TranslationOptions):
    fields = ('description', 'description_attractions',)


# @register(Gallery)
# class GalleryTranslationOptions(TranslationOptions):
#     fields = ('descriptions',)


@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(CultureGames)
class CultureGamesTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(CultureNationalClothes)
class CultureNationalClothesTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(CultureHandCrafts)
class CultureHandCraftsTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(CultureCurrency)
class CultureCurrencyTranslationOptions(TranslationOptions):
    fields = ('description',)


# @register(CultureKitchen)
# class CultureKitchenTranslationOptions(TranslationOptions):
#     fields = ('description',)


@register(CultureNationalInstruments)
class CultureNationalInstrumentsTranslationOptions(TranslationOptions):
    fields = ('description',)


# @register(Review)
# class ReviewTranslationOptions(TranslationOptions):
#     fields = ('text',)
