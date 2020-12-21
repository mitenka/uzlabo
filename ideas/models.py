from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import (
    ResizeToFill,
    Transpose,
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name='subcategories', null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField(upload_to='ideas/%Y/%m/%d/')
    idea = models.ForeignKey('Idea', on_delete=models.CASCADE,
                             related_name='images', null=True, blank=True)
    thumbnail = ImageSpecField(source='file',
                               processors=[Transpose(), ResizeToFill(1024, 768)],
                               format='JPEG',
                               options={'quality': 90})

    def __str__(self):
        return str(self.id)


class Idea(models.Model):
    STATUS_CHOICES = (
        ('on the ballot', 'On the ballot'),
        ('in developing', 'In developing'),
        ('implemented', 'Implemented'),
        ('refused', 'Refused'),
        ('banned', 'Banned'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='+')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    address = models.CharField(max_length=255)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.title)
