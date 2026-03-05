from django.contrib.auth.models import User
from django.db.transaction import atomic
from rest_framework.exceptions import ValidationError

from objectives.api.serializers import ObjectiveCreateSerializer
from objectives.models import Objective


class CreateObjectiveUseCase:
    @atomic
    def execute(
        self,
        serializer: ObjectiveCreateSerializer,
        user: User,
    ) -> None:
        objective: Objective = serializer.save(user=user)

        if objective.parent is not None and objective.parent.kind != objective.kind:
            raise ValidationError("Вид `kind` родительской цели должен совпадать с видом цели")
