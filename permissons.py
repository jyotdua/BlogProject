from rest_framework import permissions

class Is_Owner_Or_Read_Only(permissions.BasePermission):

    def has_object_permisson(selfself, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner==request.user

