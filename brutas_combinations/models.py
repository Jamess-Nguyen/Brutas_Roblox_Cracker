from django.db import models

# Database Table of Username/Password/Created 
class UserCombination(models.Model):
    username_str = models.CharField(max_length=64)
    password_str = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username_str} | {self.password_str} | {self.created_at}"
