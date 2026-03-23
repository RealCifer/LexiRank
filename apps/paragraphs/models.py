from django.db import models
from django.conf import settings


class Paragraph(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


class WordFrequency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'word')

    def __str__(self):
        return f"{self.word} ({self.count})"