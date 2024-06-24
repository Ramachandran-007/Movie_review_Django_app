from django.contrib import admin
from .models import MovieModel,CommentModel
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','comment','comment_date','user_rating','movie']

admin.site.register(MovieModel)
admin.site.register(CommentModel,CommentAdmin)