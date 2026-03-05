from typing import ClassVar

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from objectives.api.serializers import (
    ObjectiveCreateSerializer,
    ObjectiveReadSerializer,
    ObjectiveUpdateSerializer,
)
from objectives.deps import create_create_objective_use_case
from objectives.models import Objective


class ObjectivesViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete", "head", "options"]  # noqa: RUF012
    permission_classes: ClassVar = [IsAuthenticated]
    # TODO: получать только цели пользователя
    # TODO: добавить фильтр по виду цели
    queryset = Objective.objects.all().order_by("-id")

    serializer_action_classes: ClassVar = {
        "create": ObjectiveCreateSerializer,
        "update": ObjectiveUpdateSerializer,
    }
    serializer_class = ObjectiveReadSerializer

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)

    # TODO: вынести логику создания в юзкейс
    def perform_create(self, serializer):
        use_case = create_create_objective_use_case()

        use_case.execute(serializer=serializer, user=self.request.user)
