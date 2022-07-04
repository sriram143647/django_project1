from django.db import models

from django.contrib.auth import get_user_model
from team.models import Team

# Create your models here.
class Task(models.Model) :

    STATUS_ASSIGNED = "assigned"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"
    STATUS_UNDER_REVIEW = "under_review"
    STATUS_CHOICES = [
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Done'),
        (STATUS_UNDER_REVIEW, "Under Reviews")
    ]

    name = models.CharField(max_length=250)
    team = models.ForeignKey(Team, related_name="tasks", on_delete=models.CASCADE)
    members = models.ManyToManyField(get_user_model(), related_name="assigned_tasks", blank = True)
    status = models.CharField(max_length=45, choices=STATUS_CHOICES, default=STATUS_UNDER_REVIEW)

    # When team is assigned
    started_at = models.DateTimeField(null=True, default=None)

    # When Status is set to complete
    completed_at = models.DateTimeField(null=True, default=None)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

