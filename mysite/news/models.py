from django.db import models


class News(models.Model):
    title = models.CharField(
        verbose_name='Title', max_length=64
    )
    content = models.TextField(
        blank=True, verbose_name='Content'
    )
    created_at = models.DateTimeField(
        verbose_name='Created', auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name='Updated', auto_now=True
    )
    photo = models.ImageField(
        verbose_name='Image', upload_to='photos/%Y/%m/%d/'
    )
    is_published = models.BooleanField(
        verbose_name='Published', default=True
    )
