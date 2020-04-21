from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.template.defaultfilters import slugify


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    content = RichTextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my_blog:post_detail", args=[self.pk, self.slug])

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.publish <= timezone.now()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(self.title)
