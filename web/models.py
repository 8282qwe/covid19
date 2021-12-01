from django.db import models


# Create your models here.
class User_gps(models.Model):
    username = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    timestamp = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'User_gps'
        unique_together = ('username', 'x', 'y', 'timestamp')

    def __str__(self):
        return self.username + str(self.timestamp)
