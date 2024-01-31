from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False, unique=True)
    company = models.CharField(max_length=255, null=False)
    empid = models.BigIntegerField(null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=255, null=False)


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    ccode = models.BigIntegerField(null=False)
    title = models.CharField(max_length=255, null=False)
    pstatus = models.CharField(max_length=255, null=False)
    startline = models.DateField(null=False)
    deadline = models.DateField(null=False)
    profit = models.BigIntegerField(null=False)
    description = models.TextField(null=False)
    tasks = models.TextField(null=False)

class CCode(models.Model):
    id = models.AutoField(primary_key=True)
    ccode = models.BigIntegerField(null=False, unique=True)
    owner = models.CharField(max_length=255, null=False)


class AccessControl(models.Model):
    id = models.AutoField(primary_key=True)
    empid = models.BigIntegerField(null=False)
    username = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255, null=False)
    ccode = models.BigIntegerField(null=False)
    owner = models.CharField(max_length=255, null=False)
    updateaccess = models.BooleanField(null=False)
    deleteaccess = models.BooleanField(null=False)
    createaccess = models.BooleanField(null=False)