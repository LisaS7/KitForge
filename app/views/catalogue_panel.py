import flet as ft

from ..models import CatalogueItem
from . import styles


def handle_add_item(controller: "BuildController", item: CatalogueItem):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.add_item(item)

    return on_click


def build_catalogue_panel(controller: "BuildController") -> ft.Control:  # type: ignore  # noqa: F821

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
        expand=1,
        padding=styles.PANEL_PADDING,
        bgcolor=styles.SURFACE,
        border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
    )
