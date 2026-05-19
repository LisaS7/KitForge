import flet as ft

from app.controllers.build_controller import BuildController
from app.views.build.bag_panel import build_middle_panel
from app.views.build.catalogue_panel import build_catalogue_panel
from app.views.build.kit_panel import build_kit_panel
from app.views.build.stats_panel import build_stats_panel
from app.views.common import styles


def build_header() -> ft.Container:
    return ft.Container(
        bgcolor=styles.ACCENT,
        border=ft.border.only(bottom=ft.BorderSide(styles.BORDER_WIDTH, styles.TEXT)),
        padding=styles.PANEL_PADDING,
        content=ft.Row(
            controls=[
                ft.Text(
                    value="New Kit",
                    size=styles.TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(expand=True),
                ft.Button("Configure Kit"),
                ft.Button("Build"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


def build_screen(controller: BuildController) -> ft.Control:
    header = build_header()
    catalogue_panel = build_catalogue_panel(controller)
    bag_panel = build_middle_panel(controller)
    stats_panel = build_stats_panel(controller)
    kit_panel = build_kit_panel(controller)

    middle_panel = ft.Container(
        expand=True,
        border=ft.border.only(right=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
        content=ft.Column(controls=[bag_panel, stats_panel], expand=True, spacing=0),
    )

    main_content = ft.Row(
        controls=[
            catalogue_panel,
            middle_panel,
            kit_panel,
        ],
        expand=True,
        spacing=0,
    )
    controller.refresh_stats()
    return ft.Column(controls=[header, main_content], expand=True, spacing=0)
