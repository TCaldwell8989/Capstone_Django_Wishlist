from django.db import models
from django.utils import timezone

# Create a database model with four columns
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)
    visited_date = models.DateField(blank=True, null=True)


    def visited_on(self):
        self.visited_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)