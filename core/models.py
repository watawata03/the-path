from django.db import models


class Work(models.Model):
    MEDIA_CHOICES = [
        ('movie', '映画'),
        ('series', 'ドラマ'),
        ('anime', 'アニメ'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    beginner_level = models.IntegerField()

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    works = models.ManyToManyField(Work, related_name="characters")

    def __str__(self):
        return self.name


class Route(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    works = models.ManyToManyField(Work, related_name="routes")

    def __str__(self):
        return self.title