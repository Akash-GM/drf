from .permissions import IsStaffEditorPermissions
from rest_framework import permissions


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class UserQuerySetMixin:
    user_field = "user"
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs

        lookup_data = {}
        lookup_data[self.user_field] = user
        print("the lookup data {} ".format(lookup_data))

        return qs.filter(**lookup_data)
