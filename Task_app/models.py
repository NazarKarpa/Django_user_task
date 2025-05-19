from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS = (
    ('in proceed', 'Адміністратор'),
    ('well done', 'Користувач'),
    ('postpone', 'Відкладено')
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices= STATUS, default='in proceed')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
