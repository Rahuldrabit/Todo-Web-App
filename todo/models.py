from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    sno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']