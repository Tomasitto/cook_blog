from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.

class RecipeInLIne(admin.StackedInline):
    model = models.Recipe
    extra = 1 #добавлять всего 1 рецепт к посту


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'categoty', 'create_at', 'id']
    inlines = [RecipeInLIne]

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
