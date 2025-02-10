from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from dj_rest_auth.views import LogoutView
from rest_framework.response import Response
from rest_framework import status


class CustomLogoutView(LogoutView):
    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "refresh": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    title="Refresh",
                    description="Logout with blacklist Refresh token",
                    min_length=1,
                )
            },
            required=["refresh"],
        ),
    )
    def post(self, request, *args, **kwargs):
        if request.data.get("refresh", None):
            return super().post(request, *args, **kwargs)

        return Response(
            {"detail": _("Refresh token was not included in request data.")},
            status=status.HTTP_400_BAD_REQUEST,
        )