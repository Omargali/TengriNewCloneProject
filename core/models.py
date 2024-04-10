from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('featured', 'Избранные'),
        ('politics', 'Политика'),
        ('business_economy', 'Бизнес и экономика'),
        ('culture', 'Культура'),
        ('technology', 'Технологии'),
        ('sports', 'Спорт'),
        ('education', 'Образование'),
    ]

    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    body = RichTextUploadingField(verbose_name='Содержание поста')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
