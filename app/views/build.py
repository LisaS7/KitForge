import flet as ft

from app.controllers.build_controller import BuildController
from app.views.catalogue_panel import build_catalogue_panel
from app.views.kit_panel import build_kit_panel
from app.views.middle_panel import build_middle_panel

from ..models import CatalogueItem, Category, Kit
from . import styles


def build_header() -> ft.Control:
    return ft.Column(
        [
            ft.Text(
                "KitForge",
                size=styles.TITLE_SIZE,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Text("Emergency kit planner"),
        ]
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
        controls=[catalogue_panel, middle_panel, kit_panel],
        expand=True,
        spacing=styles.SECTION_SPACING,
    )

    return ft.Column(
        controls=[header, main_content], expand=True, spacing=styles.SECTION_SPACING
    )
