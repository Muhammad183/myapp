from django.db import models


class Buy(models.Model):
    first_name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    phone_num = models.IntegerField(null = True)

    class Meta:
        verbose_name = ("buy")
        verbose_name_plural = ("buy")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("buy", kwargs={"pk": self.pk})


class Region(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

