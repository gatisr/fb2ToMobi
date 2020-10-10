from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255, blank=True)
    book = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    converted_book = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name