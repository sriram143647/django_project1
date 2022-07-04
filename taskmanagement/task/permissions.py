from django.conf import settings
from rest_framework import permissions

class UserAllowedUpdate(permissions.BasePermission) :

    def has_permission(self, request, view):
        user_role = [g.name for g in request.user.groups.all()]

        if settings.GROUP_TEAM_MEMEBER in user_role:
            if "staus" in request.data and len(request.data) == 1 :
                return True
            else :
                return False
        
        return True

class IsUserRole(permissions.BasePermission) :
    
    def has_permission(self, request, view):
        user_role = [g.name for g in request.user.groups.all()]
        if settings.GROUP_USER in user_role:
            return True
        return False
        



