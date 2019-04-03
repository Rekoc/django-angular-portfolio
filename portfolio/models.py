from django.db import models
from django.template.defaultfilters import slugify


class ImageField(models.Model):
    image = models.ImageField(upload_to="{}".format("images"))
    title = models.CharField(max_length=100, default="", blank=True)
    sub_title = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        # Display title in Django Admin
        return self.image


class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True, max_length=100, editable=False, default="")

    creation_date = models.DateTimeField(auto_now_add=True, auto_created=True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    is_displayed = models.BooleanField('Display it, or not', default=True)

    view = models.IntegerField(default=0, editable=False)
    description = models.TextField(max_length=1000, blank=True, default="")

    image1 = models.ImageField(upload_to="{}".format(slug))
    image2 = models.ImageField(upload_to="{}".format(slug), blank=True)
    image3 = models.ImageField(upload_to="{}".format(slug), blank=True)

    class Meta:
        ordering = ["update_date"]
        verbose_name = "Portfolio Item"
        verbose_name_plural = "Portfolio Items"

    def __str__(self):
        # Display title in Django Admin
        return self.title

    def save(self, *args, **kwargs):
        # Update the slug variable and save it
        self.slug = slugify(self.title)
        super(PortfolioItem, self).save(*args, **kwargs)

    def add_one_view(self):
        self.view += 1
        self.save()
