from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,null=True, blank=True)
    article = HTMLField()
    adminID = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Tự động lấy thời gian tạo
    updated_at = models.DateTimeField(auto_now=True)
def __str__(self):
    return self.title
# Create your models here.
