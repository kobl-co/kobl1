from django.db import models
from django.utils import timezone


class Card(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    contact_person = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    functional_location = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    status = models.CharField(max_length = 200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def approve(self):
        self.status = "Approved"
        self.save()
    def reject(self):
        self.status = "Rejected"
        self.save()
    def checked(status):
        self.status = "Checked"
        self.save()

    def __str__(self):
        return self.title