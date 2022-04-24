from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name = 'article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500) # 把url之间的空格换成短线来弄
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE,
                               related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now) # 默认的文章发布时间
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("title", )
        index_together = (('id', 'slug')) # 对数据库这两个字段建立索引，在后面，会通过每篇文章的id和slug获取该文章对象

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """要得到相应文章的路径"""
        return reverse("article:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        """获取url的反射"""
        return reverse("article:article_content", args=[self.id, self.slug])


