from django.db import models

# from django.db.models.signals import post_save
# from django.dispatch import receiver

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

# @receiver(post_save, sender=Post)
# def send_post_creation_notification(sender, instance, created, **kwargs):
#     if created:
#         subject = 'New Post Created'
#         message = f'Hi {instance.author.username},\n\nA new post "{instance.title}" has been created.'
#         send_mail(subject, message, 'your-email@example.com', [instance.author.email])
    