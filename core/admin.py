from django.contrib import admin
from core.models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'work_status', 'short_description', 'updated_date', 'created_date']
    search_fields = ['name', 'surname']
    list_editable = ['work_status',]

    def short_description(self, obj):
        return obj.description[:30] + '...' if len(obj.description) > 30 else obj.description
    short_description.short_description = 'Description'  # Admin başlığı

    class Meta:
        model = About







@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'proccess_color', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['percentage', 'proccess_color']

    class Meta:
        model = Skill



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['image']

    class Meta:
        model = Images        




@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    filter_horizontal = ('skills',)  # ManyToMany ilişkisi için
    class Meta:
        model = Service

@admin.register(ServicesName)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    
    class Meta:
        model = ServicesName    