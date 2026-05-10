import flet as ft

from app.controllers.build_controller import BuildController
from app.views.catalogue_panel import build_catalogue_panel
from app.views.kit_panel import build_kit_panel
from app.views.middle_panel import build_middle_panel

from ..models import CatalogueItem, Category, Kit
from . import styles


def build_header() -> ft.Container:
    return ft.Container(
        bgcolor=styles.ACCENT,
        border=ft.border.only(bottom=ft.BorderSide(styles.BORDER_WIDTH, styles.TEXT)),
        padding=styles.PANEL_PADDING,
        content=ft.Row(
            controls=[
                ft.Text(
                    "New Kit",
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


def build_screen(
    page: ft.Page, categories: dict[Category, list[CatalogueItem]], kit: Kit
) -> ft.Control:
    controller = BuildController(page, kit, categories)

    header = build_header()
    catalogue_panel = build_catalogue_panel(controller)
    middle_panel = build_middle_panel(controller)
    kit_panel = build_kit_panel(controller)

    main_content = ft.Row(
        controls=[catalogue_panel, middle_panel, kit_panel], expand=True, spacing=0
    )

    return ft.Column(
        controls=[header, main_content], expand=True, spacing=0
    )
