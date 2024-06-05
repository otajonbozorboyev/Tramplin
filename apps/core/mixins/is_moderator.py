from rest_framework import status
from rest_framework.response import Response

class ModeratorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_moderator:
            return Response(
                {"error": "You must be a moderator to access this endpoint."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().dispatch(request, *args, **kwargs)