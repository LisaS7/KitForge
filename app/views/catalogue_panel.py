import flet as ft

from app.views.icons import CATEGORY_ICONS

from ..models import CatalogueItem, Category
from . import styles


def handle_add_item(controller: "BuildController", item: CatalogueItem):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.add_item(item)

    return on_click


def handle_select_category(controller: "BuildController", category: Category):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.select_category(category)

    return on_click


def category_tile(category: Category, on_click) -> ft.Container:
    # return a clickable category tile
    # category, icon, click handler
    # styling
    return ft.Container(
        width=styles.TILE_SIZE,
        height=styles.TILE_SIZE,
        padding=styles.ITEM_SPACING,
        bgcolor=styles.BACKGROUND,
        border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
        on_click=on_click,
        content=ft.Column(
            controls=[
                ft.Icon(
                    CATEGORY_ICONS[category], size=styles.ICON_SIZE, color=styles.TEXT
                ),
                ft.Text(
                    category.value,
                    size=styles.LABEL_SIZE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=styles.ITEM_SPACING,
        ),
    )


def build_category_grid(controller: "BuildController") -> ft.GridView:  # type: ignore  # noqa: F821
    # return a grid of cat buttons
    return ft.GridView(
        controls=[
            category_tile(
                category, on_click=handle_select_category(controller, category)
            )
            for category in controller.categories
        ],  # type: ignore
        runs_count=3,
        max_extent=100,
        child_aspect_ratio=1,
        spacing=styles.ITEM_SPACING,
        run_spacing=styles.ITEM_SPACING,
    )


def build_catalogue_panel(controller: "BuildController") -> ft.Control:  # type: ignore  # noqa: F821

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "CATALOGUE", size=styles.PANEL_TITLE_SIZE, weight=ft.FontWeight.BOLD
                ),
                build_category_grid(controller),
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        width=styles.CATALOGUE_WIDTH,
        padding=styles.PANEL_PADDING,
        bgcolor=styles.SURFACE,
        border=ft.border.only(right=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
    )
