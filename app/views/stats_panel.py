from typing import TYPE_CHECKING

import flet as ft

from app.stats import KitStats
from app.views import styles

if TYPE_CHECKING:
    from app.controllers.build_controller import BuildController


def build_stats_panel(controller: "BuildController") -> ft.Container:
    stats_panel = ft.Container(
        expand=False,
        bgcolor=styles.SURFACE,
        border=ft.border.only(top=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
        padding=styles.PANEL_PADDING,
        content=ft.Row(controls=[], alignment=ft.MainAxisAlignment.START),
    )

    controller.stats_panel = stats_panel
    return stats_panel


def build_stats_controls(stats: KitStats) -> list[ft.Control]:
    return [
        ft.Text(f"Weight: {stats.total_weight_g}g / {stats.weight_limit_g}g"),
        ft.Text(f"Calories: {stats.total_calories} kcal"),
        ft.Text(f"Water: {stats.stored_water_ml} ml"),
        ft.Text(f"Readiness: {stats.readiness_score}%"),
    ]
