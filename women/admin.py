from typing import Any
from django.contrib import admin, messages
from .models import Women, Category
from django.utils.safestring import mark_safe

class MarriedFilter(admin.SimpleListFilter):
    title = 'Ayol statusi'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Erga chiqqan'),
            ('not_married', 'Erga chiqmagan'),
        ]

    def queryset(self, request, queryset) :
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'not_married':
            return queryset.filter(husband__isnull=True)

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content','photo', 'post_photo', 'cat', 'husband', 'tags']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    #filter_vertical = ('tags',)
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 3
    actions= ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Qisqacha tavsifi', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Rasmsiz"
    

    @admin.action(description='Nashr qiling')
    def set_published(self, request, queryset):
        count= queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'{count} ayollar nashr qilingan')

    @admin.action(description='Nashrdan olib tashlang')
    def set_draft(self, request, queryset):
        count= queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} ayollar nashr olib tashlangan', messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links= ('id', 'name')