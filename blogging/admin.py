from django.contrib import admin

# a new import
from blogging.models import Post, Category

class CategoryInline(admin.StackedInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)