import django_setup
from User_app.models import User1, Group
from Task_app.models import Task, User

#group = Group(name = 'Teacher')
#group.save()

#user = User.objects.create(name ='admin',
#                           email='admin@gmail.com', role='admin')

#user2 = User.objects.create(name ='user',
#                           email='user@gmail.com')

# Створення користувачів
#user1 = User.objects.create(name="Іван Петренко")
#user2 = User.objects.create(name="Олена Коваль")

# Створення завдань
#task1 = Task.objects.create(
#    name="Підготувати звіт",
#    description="Зібрати статистику за останній місяць.",
#    status="in proceed",
#    user=user1
#)

#task2 = Task.objects.create(
#    name="Перевірити пошту",
#    description="Відповісти на листи від клієнтів.",
#   status="well done",
#   user=user2
#)

#task3 = Task.objects.create(
#    name="Запланувати зустріч",
#    description="Організувати зустріч з командою на наступний тиждень.",
#    status="postpone",
#    user=None  # Без призначеного користувача
#)
