from django.db import models


NATIONALITY_CHOICES = (
    ('ARG', 'Argentina'),
    ('BRAZIL', 'Brasil'),
    ('USA', 'Estados Unidos'),
)


class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
