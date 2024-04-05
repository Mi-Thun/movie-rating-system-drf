from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Movie, Rating
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'phone')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'phone') 

class CustomUserAdmin(UserAdmin):
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )
    list_display = ['name', 'email', 'phone', 'is_staff'] 
    search_fields = ('email', 'phone')
    ordering = ('email',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'rating', 'release_date')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'movie_id', 'rating')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
