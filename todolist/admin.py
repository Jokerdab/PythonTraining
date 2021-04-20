from django.contrib import admin

from .models import Card, Progress_type, Category, Chapter

class CardAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "created", "category", "progress_type")

    search_fields = ("title", "subtitle", "category")
    list_filter = ("created",)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

class Progress_typeAdmin(admin.ModelAdmin):
    list_display = ("type_of_progress",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("type_category",)


admin.site.register(Card,CardAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Progress_type, Progress_typeAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
