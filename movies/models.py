from django.db import models


class Movie(models.Model):
    """
    Movies model
    """

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Movies"