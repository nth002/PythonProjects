from django.db import models

# Create your models here.

class Users(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=100, null=True, blank=True)
    u_password = models.CharField(max_length=100, null=True, blank=True)
    u_name = models.CharField(max_length=100, null=True, blank=True)
    u_dob = models.CharField(max_length=100, null=True, blank=True)
    u_gender = models.CharField(max_length=100, null=True, blank=True)
    u_email = models.CharField(max_length=100, null=True, blank=True)
    u_mobile_num = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table="users"