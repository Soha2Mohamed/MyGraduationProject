from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    email = models.EmailField()
    #followerIds = models.ForeignKey(on_delete=models.CASCADE, null=True)
    #followerIDs = models.ManyToManyField('self', related_name='following')
    #followingsIds = models.ManyToManyField('self', related_name='following')
    chatIds = models.CharField()
    socket_ids = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class FollowerShip(models.Model):
    user_id = models.ForeignKey(User, related_name="following")

    following_user_id = models.ForeignKey("User", related_name="followers")


class Messages(models.Model):
    message = models.TextField(max_length=None)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    chat_id = models.ForeignKey(User, related_name="chat",  on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=20)
    time= models.DateTimeField(auto_now_add=True)
