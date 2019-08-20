from django.db import models

# Create your models here.
class BankMerch(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length =60)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
