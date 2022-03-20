from django import forms
from django.contrib import admin

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AnimeAdminForm(forms.ModelForm):
    hep = forms.CharField(label='Видео с ютуб', widget=CKEditorUploadingWidget())

    class Meta:
        model = Anime
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "url")
    list_display_links = ("name", 'id')
    prepopulated_fields = {'url': ('name',)}


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    prepopulated_fields = {'url': ('title',)}
    form = AnimeAdminForm


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "anime", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    prepopulated_fields = {'url': ('name',)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    pass




