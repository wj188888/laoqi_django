from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    # 防止硬编码
    path('blog/', include('blog.urls', namespace='blog')),
    path('account/', include('account.urls', namespace='account')),
    path('article/', include('article.urls', namespace='article')),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),

]
