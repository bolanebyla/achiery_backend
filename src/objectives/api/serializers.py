from typing import ClassVar

from rest_framework import serializers

from objectives.models import Objective


class ObjectiveCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания цели"""

    class Meta:
        model = Objective
        fields: ClassVar = [
            "title",
            "description",
            "difficulty",
            "kind",
            "target_value",
            "current_value",
            "parent_id",
        ]


class ObjectiveUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения цели"""

    class Meta:
        model = Objective
        fields: ClassVar = [
            "title",
            "description",
            "difficulty",
            "target_value",
        ]


class ObjectiveReadSerializer(serializers.ModelSerializer):
    """Сериализатор для создания цели"""

    class Meta:
        model = Objective
        fields: ClassVar = [
            "id",
            "title",
            "description",
            "difficulty",
            "target_value",
            "current_value",
            "parent_id",
            "completed_at",
        ]
