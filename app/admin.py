from django.contrib import admin
from .models import Users, Tasks, CCode, AccessControl

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'username', 'company', 'empid', 'email']

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'ccode', 'title', 'pstatus', 'startline', 'deadline', 'profit', 'description', 'tasks']

@admin.register(CCode)
class CCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ccode', 'owner']

@admin.register(AccessControl)
class AccessControlAdmin(admin.ModelAdmin):
    list_display = ['id', 'empid', 'username', 'company', 'ccode', 'owner', 'updateaccess', 'deleteaccess', 'createaccess']
