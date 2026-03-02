from django.contrib import admin

from objectives.models import Objective


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "kind",
        "user",
        "title",
        "description",
        "current_value",
        "target_value",
        "difficulty",
    )

    list_filter = ("kind", "user")


