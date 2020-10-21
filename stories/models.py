from django.db import models


class Story(models.Model):
    """
    Story model
    """

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Stories"