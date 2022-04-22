from django.contrib import admin
from .models import ArticleColumn

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created', 'user')
    list_filter = ("column", )

# 文章注册
admin.site.register(ArticleColumn, ArticleColumnAdmin)
