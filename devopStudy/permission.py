from rest_framework.permissions import DjangoModelPermissions


class Permission(DjangoModelPermissions):

    def get_extra_perms(self,method, view):
        if hasattr(view, 'extra_perms_map'):
            if isinstance(view.extra_perms_map, dict):
                return view.extra_perms_map.get(method, [])
        return []

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        perms.extend(self.get_extra_perms(request.method, view))
        # if not perms:
        #     perms = ['deny']
        print(perms)
        return request.user.has_perms(perms)
