from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Movie, Rating


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'rating', 'release_date')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
