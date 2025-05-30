"""
Views for users app.
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def placeholder_view(request):
    """
    Placeholder view for users app.
    """
    return Response({"message": "Users API is coming soon!"})