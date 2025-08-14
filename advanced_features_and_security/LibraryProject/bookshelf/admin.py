from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year' )
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_superuser")


admin.site.register( Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)