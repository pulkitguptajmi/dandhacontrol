from rest_framework import permissions

class CustomObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Your custom permission logic here, e.g., check if the user is the owner of the object
        #api
        request.client_id = "xyz"