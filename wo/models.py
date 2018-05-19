from django.db import models
from django.utils import timezone


class Wo(models.Model):
    
    wo_number = models.AutoField(primary_key=True, max_length=8)
    planner_id = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    functional_location = models.CharField(max_length=200)
#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
    status = models.CharField(max_length = 200)
    status_report = models.TextField()

    def work_ongoing(self):
        self.status = "Ongoing"
        self.save()
    def work_completed(self):
        self.status = "Completed"
        self.save()
    def work_partially_completed(status):
        self.status = "Partial"
        self.save()

    def __str__(self):
        return self.title