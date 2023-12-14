from django.db import models
from django.utils import timezone

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    contents = models.TextField()
    creation_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    restricted = models.BooleanField(default=False)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)

    def __str__(self):
        return "Document {} {} {}.".format(self.title, self.subtitle, self.domain)


class Domain(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Domain', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Account(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['domain', 'user'], name='unique_domain_user'),
        ]

    def __str__(self):
        return "{}@{}".format(self.user, self.domain)