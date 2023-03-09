from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=1000)
    position = models.CharField(max_length=10000)
    grade = models.IntegerField()

    def __str__(self) -> str:
        return "{0} | {1}".format(self.name, self.position)

    class Meta:
        ordering = ("name",)