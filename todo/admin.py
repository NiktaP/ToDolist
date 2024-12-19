from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed', 'created_at','last_update']
    list_filter = ['is_completed']
    search_fields = ['title']

admin.site.register(Todo, TodoAdmin)
