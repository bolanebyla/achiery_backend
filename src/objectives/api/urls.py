from rest_framework import routers

from objectives.api.views import ObjectivesViewSet

objectives_api_router = routers.SimpleRouter()

objectives_api_router.register("objectives", ObjectivesViewSet)
