from rest_framework import permissions

#관리자임 소유자임?
class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_supperuser

#관리자임 소유자임+ 세이프메소드(->수정안한 매소드)안에 들어가있음?
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_supperuser

