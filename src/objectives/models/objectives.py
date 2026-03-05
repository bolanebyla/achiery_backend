from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class ObjectiveKinds(models.TextChoices):
    """Виды целей"""

    ACHIEVEMENT = "ACHIEVEMENT", "Ачивка"
    QUEST = "QUEST", "Квест"
    # TODO: CHALLENGE = "CHALLENGE", "Вызов"


class Objective(models.Model):
    """Цель"""

    id = models.AutoField(primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    title: str = models.TextField(
        verbose_name="Название",
        db_comment="Название",
    )
    description: str = models.TextField(
        verbose_name="Описание",
        db_comment="Описание",
    )

    difficulty: int = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4)],
        verbose_name="Сложность",
        db_comment="Сложность",
    )

    kind: ObjectiveKinds = models.TextField(
        choices=ObjectiveKinds.choices,
        verbose_name="Вид цели",
        db_comment="Вид цели",
    )

    target_value: int = models.IntegerField(
        verbose_name="Необходимо для выполнения",
        db_comment="Необходимо для выполнения",
    )
    current_value: int = models.IntegerField(
        verbose_name="Текущее значение",
        db_comment="Текущее значение",
    )

    parent: "Objective" = models.ForeignKey(
        "Objective",
        on_delete=models.PROTECT,
        null=True,
    )

    completed_at: datetime = models.DateTimeField(null=True)
    archived_at: datetime = models.DateTimeField(null=True)

    class Meta:
        db_table = "objectives"
        db_table_comment = "Цели"
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    def __str__(self) -> str:
        return str(self.id)
