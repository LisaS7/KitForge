from typing import TYPE_CHECKING

import flet as ft

from app.stats import KitStats
from app.views.common import styles

if TYPE_CHECKING:
    from app.controllers.build_controller import BuildController


def build_stats_panel(controller: "BuildController") -> ft.Container:
    stats_panel = ft.Container(
        expand=False,
        bgcolor=styles.SURFACE,
        border=ft.border.only(top=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
        padding=styles.PANEL_PADDING,
        content=ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=styles.SECTION_SPACING,
        ),
    )

    controller.stats_panel = stats_panel
    return stats_panel


def build_stats_controls(stats: KitStats) -> list[ft.Control]:
    weight_bar = ft.Column(
        spacing=2,
        controls=[
            ft.Text("Weight"),
            ft.Text(
                f"{stats.total_weight_kg():.1f} kg / {stats.weight_limit_kg():.1f} kg"
            ),
            ft.ProgressBar(
                value=stats.weight_percentage,  # type: ignore
                color=stats.weight_bar_colour,
                width=120,
            ),
        ],
    )

    calories = ft.Column(
        spacing=2,
        controls=[
            ft.Text("Calories"),
            ft.Text(f"{stats.total_calories} / {stats.calorie_requirement} kcal"),
        ],
    )

    water = ft.Column(
        spacing=2,
        controls=[
            ft.Text("Water"),
            ft.Text(
                f"{stats.stored_water_l():.1f} / {stats.water_requirement_l():.1f} L"
            ),
        ],
    )

    readiness = ft.Column(
        spacing=2,
        controls=[
            ft.Text("Readiness"),
            ft.Text(f"{stats.readiness_score}%"),
        ],
    )

    return [weight_bar, calories, water, readiness]
