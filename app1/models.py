from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
