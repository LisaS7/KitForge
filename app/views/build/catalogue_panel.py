from typing import TYPE_CHECKING

import flet as ft

from app.views.common import styles
from app.views.common.icons import CATEGORY_ICONS

from ...models import CatalogueItem, Category

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


def category_tile(category: Category, on_click, is_covered: bool) -> ft.Container:
    label_controls: list[ft.Control] = [
        ft.Text(
            category.value,
            size=styles.LABEL_SIZE,
            text_align=ft.TextAlign.CENTER,
        )
    ]

    if not is_covered:
        label_controls.append(
            ft.Icon(
                ft.Icons.WARNING_ROUNDED,
                size=styles.LABEL_SIZE,
                color=styles.WARNING,
            )
        )

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
                    CATEGORY_ICONS[category],
                    size=styles.ICON_SIZE,
                    color=styles.TEXT,
                ),
                ft.Row(
                    controls=label_controls,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=2,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=styles.ITEM_SPACING,
        ),
    )


def item_tile(item: CatalogueItem, on_click) -> ft.Container:
    item_name = ft.Text(
        item.name, size=styles.LABEL_SIZE, text_align=ft.TextAlign.CENTER
    )
    item_weight = ft.Text(
        f"{item.weight_g}g",
        size=styles.LABEL_SIZE,
        color=styles.MUTED_TEXT,
        text_align=ft.TextAlign.CENTER,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                item_name,
                item_weight,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        height=styles.TILE_SIZE,
        width=styles.TILE_SIZE,
        ink=True,
        on_click=on_click,
        padding=styles.TILE_PADDING,
        border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
        bgcolor=styles.BACKGROUND,
    )


def build_category_grid(controller: "BuildController") -> ft.GridView:
    tiles: list[ft.Control] = [
        category_tile(
            category,
            on_click=handle_select_category(controller, category),
            is_covered=controller.is_category_covered(category),
        )
        for category in controller.categories
    ]
    return ft.GridView(
        controls=tiles,
        runs_count=2,
        max_extent=100,
        child_aspect_ratio=1,
        spacing=styles.ITEM_SPACING,
        run_spacing=styles.ITEM_SPACING,
        padding=styles.PANEL_PADDING,
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

    item_grid = ft.GridView(
        controls=[
            item_tile(item, on_click=handle_add_item(controller, item))
            for item in items
        ],
        runs_count=3,
        max_extent=100,
        child_aspect_ratio=1,
        spacing=styles.ITEM_SPACING,
        run_spacing=styles.ITEM_SPACING,
        padding=styles.PANEL_PADDING,
    )

    help_note = ft.Container(
        ft.Text(
            # TODO: change helper text once drag & drop is done
            "Click item to add",
            size=styles.LABEL_SIZE,
            color=styles.MUTED_TEXT,
            italic=True,
        ),
        padding=styles.PANEL_PADDING,
    )

    return ft.Column(controls=[back_button, item_grid, help_note])


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
