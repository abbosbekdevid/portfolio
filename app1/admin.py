from django.contrib import admin

# Register your models here.


from .models import ProfileModel, ProjectModel, BlogModel, SkillModel, CategoryModel, ServiceModel

admin.site.register(ProjectModel)


@admin.register(ProfileModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (  'id', 'full_name' ,)
    list_display_links = ('id', 'full_name',)
    search_fields = ( 'id', 'full_name' ,)
    list_filter = (  'id', 'full_name' ,)

@admin.register(ServiceModel)
class ServiesAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'order', )
    list_editable = ('order',)
    search_fields = ('name', 'order',)
    list_filter =  ( 'name', 'order', )

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'published_at', 'author', )
    list_display_links = ( 'title', 'author',)
    list_filter = ( 'title', 'published_at', 'author',)
    search_fields = ('author', 'title', 'published_at', )


@admin.register(CategoryModel)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter  =( 'name',)

@admin.register(SkillModel)
class SkilsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'percentage','order' ,)
    list_display_links = ( 'name',)
    search_fields = ( 'name', 'percentage','order',)
    list_editable = ( 'percentage','order',)
    list_filter = ( 'name', 'percentage','order' ,)





