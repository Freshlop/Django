from django.db import models


# Create your models here.


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(default=0.0)
    # hashtags = models.ManyToManyField(Hashtag)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=265)
    posts = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
