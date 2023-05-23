from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #Foreign key
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,related_name="posts", default=1)
    title = models.CharField(max_length=250)
    
    content = models.TextField()
    imageUrl = models.TextField(default="https://images.unsplash.com/photo-1545239351-ef35f43d514b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80")
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    #Foreign key
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    #Options 
    status = models.CharField(
        max_length=10, choices=options, default='published')
    
    objects = models.Manager()  # default manager
     
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title