from typing import TYPE_CHECKING

import flet as ft

from app.views.icons import CATEGORY_ICONS

from ..models import CatalogueItem, Category
from . import styles

if TYPE_CHECKING:
    from app.controllers.build_controller import BuildController


def handle_add_item(controller: "BuildController", item: CatalogueItem):
    def on_click(e):
        controller.add_item(item)

    return on_click


def handle_select_category(controller: "BuildController", category: Category):
    def on_click(e):
        controller.select_category(category)

    return on_click


def category_tile(category: Category, on_click) -> ft.Container:
    return ft.Container(
        width=styles.TILE_SIZE,
        height=styles.TILE_SIZE,
        padding=styles.TILE_PADDING,
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


def item_tile(item: CatalogueItem, on_click) -> ft.Container:
    return ft.Container(
        content=ft.Text(item.name, size=styles.BODY_SIZE),
        on_click=on_click,
        padding=styles.TILE_PADDING,
        border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
        bgcolor=styles.BACKGROUND,
    )


def build_category_grid(controller: "BuildController") -> ft.GridView:
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


def build_item_list(controller: "BuildController", category: Category) -> ft.Control:
    items = controller.categories[category]

    back_button = ft.Container(
        content=ft.Text(f"← {category.value}", size=styles.BODY_SIZE),
        on_click=lambda e: controller.clear_selected_category(),
        padding=styles.PANEL_PADDING,
        bgcolor=styles.SURFACE,
        border=ft.border.only(bottom=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
    )

    return ft.Column(
        controls=[
            back_button,
            *[
                item_tile(item, on_click=handle_add_item(controller, item))
                for item in items
            ],
        ]
    )


def build_catalogue_panel(controller: "BuildController") -> ft.Control:
    controller.catalogue_column = ft.Column(
        controls=[build_category_grid(controller)], scroll=ft.ScrollMode.AUTO
    )

    return ft.Container(
        content=controller.catalogue_column,
        width=styles.CATALOGUE_WIDTH,
        padding=styles.PANEL_PADDING,
        bgcolor=styles.SURFACE,
        border=ft.border.only(right=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER)),
    )
