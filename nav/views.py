from rest_framework import viewsets
from .models import Waypoint
from .serializers import WaypointSerializer
from drf_spectacular.utils import OpenApiParameter, extend_schema

# Create your views here.
class WaypointViewset(viewsets.ModelViewSet):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(WaypointViewset, self).get_serializer(*args, **kwargs)