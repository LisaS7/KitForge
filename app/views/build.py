import flet as ft

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


def build_catalogue(categories: dict[Category, list[CatalogueItem]]) -> ft.Control:

    grouped_catalogue_items: list[ft.Control] = []
    for category, items in categories.items():
        grouped_catalogue_items.append(
            ft.Text(
                category, size=styles.CATEGORY_TITLE_SIZE, weight=ft.FontWeight.BOLD
            )
        )

        for item in items[:3]:
            grouped_catalogue_items.append(ft.Text(f"- {item.name}"))

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


def build_kit_panel(kit: Kit) -> ft.Control:
    if not kit.items:
        item_controls = [ft.Text("No items packed yet!", italic=True)]
    else:
        item_controls = [ft.Text(f"{item.item_id} x {item.qty}") for item in kit.items]

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Kit List",
                    size=styles.PANEL_TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                ),
                *item_controls,
            ]
        ),
        expand=1,
    )


def build_screen(
    categories: dict[Category, list[CatalogueItem]], kit: Kit
) -> ft.Control:
    header = build_header()
    catalogue_panel = build_catalogue(categories)
    kit_panel = build_kit_panel(kit)

    main_content = ft.Row(
        controls=[catalogue_panel, kit_panel],
        expand=True,
        spacing=styles.SECTION_SPACING,
    )

    return ft.Column(
        controls=[header, main_content], expand=True, spacing=styles.SECTION_SPACING
    )
