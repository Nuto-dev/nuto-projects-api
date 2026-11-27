from django.db import models


class WorkSpace(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='workspaces')

    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.__str__() + self.name