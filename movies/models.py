from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50, null=False)
    date_released = models.DateTimeField(null=False)

    class Meta:
        verbose_name: "movie"
        verbose_name_plural: "movies"

    def __str__(self):
        return f'Фильм: {self.title} | number: {self.id}'

