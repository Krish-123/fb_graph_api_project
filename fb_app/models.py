from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    access_token = models.TextField()
    issued_at = models.IntegerField()
    data_access_expires_at = models.IntegerField()
    token_expires_at = models.IntegerField()
    scopes = models.TextField()

    def __repr__(self):
        return self.user_id