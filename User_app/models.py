from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User1(models.Model):
    ROLES = (
    ('admin', 'Адміністратор'),
    ('user', 'Користувач')

    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices= ROLES, default='user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name





