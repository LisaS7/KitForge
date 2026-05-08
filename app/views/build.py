import flet as ft

from app.controllers.build_controller import BuildController
from app.views.kit_panel import build_kit_panel

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


def handle_add_item(controller: BuildController, item: CatalogueItem):
    def on_click(e):
        controller.add_item(item)

    return on_click


def build_catalogue(controller: BuildController) -> ft.Control:

    grouped_catalogue_items: list[ft.Control] = []
    for category, items in controller.categories.items():
        grouped_catalogue_items.append(
            ft.Text(
                category, size=styles.CATEGORY_TITLE_SIZE, weight=ft.FontWeight.BOLD
            )
        )

        for item in items[:3]:
            grouped_catalogue_items.append(
                ft.Button(
                    content=item.name,
                    on_click=handle_add_item(controller, item),
                )
            )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Catalogue", size=styles.PANEL_TITLE_SIZE, weight=ft.FontWeight.BOLD
                )
            ]
            + grouped_catalogue_items,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=2,
        padding=styles.PANEL_PADDING,
        bgcolor=styles.SURFACE,
        border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
    )


def build_screen(
    page: ft.Page, categories: dict[Category, list[CatalogueItem]], kit: Kit
) -> ft.Control:
    controller = BuildController(page, kit, categories)

    header = build_header()
    catalogue_panel = build_catalogue(controller)
    kit_panel = build_kit_panel(controller)

    main_content = ft.Row(
        controls=[catalogue_panel, kit_panel],
        expand=True,
        spacing=styles.SECTION_SPACING,
    )

    return ft.Column(
        controls=[header, main_content], expand=True, spacing=styles.SECTION_SPACING
    )
