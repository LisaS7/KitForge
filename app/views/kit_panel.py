from typing import TYPE_CHECKING

import flet as ft

from app.views import styles

if TYPE_CHECKING:
    from app.controllers.build_controller import BuildController


def handle_increment(controller: "BuildController", item_id: str):
    def on_click(e):
        controller.increment_item(item_id)

    return on_click


def handle_decrement(controller: "BuildController", item_id: str):
    def on_click(e):
        controller.decrement_item(item_id)

    return on_click


def handle_remove(controller: "BuildController", item_id: str):
    def on_click(e):
        controller.remove_item(item_id)

    return on_click


def build_qty_button(text: str, on_click) -> ft.Control:
    return ft.Container(
        content=ft.Text(text, size=12),
        width=22,
        height=22,
        alignment=ft.Alignment(0, 0),
        border=ft.border.all(1, styles.BORDER),
        bgcolor=styles.SURFACE,
        on_click=on_click,
    )


def build_kit_controls(controller: "BuildController") -> list[ft.Control]:
    if not controller.kit.items:
        return [ft.Text("No items packed yet!", italic=True)]

    controls: list[ft.Control] = []

    for item in controller.kit.items:
        catalogue_item = controller.get_catalogue_item(item.item_id)
        controls.append(
            ft.Row(
                controls=[
                    ft.Text(catalogue_item.name, expand=True, size=12),
                    build_qty_button("−", handle_decrement(controller, item.item_id)),
                    ft.Text(
                        str(item.qty), width=20, text_align=ft.TextAlign.CENTER, size=12
                    ),
                    build_qty_button("+", handle_increment(controller, item.item_id)),
                    build_qty_button("×", handle_remove(controller, item.item_id)),
                ]
            )
        )

    return controls


def build_kit_panel(controller: "BuildController") -> ft.Control:
    controller.kit_column = ft.Column(build_kit_controls(controller))

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "KIT LIST",
                    size=styles.PANEL_TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                ),
                controller.kit_column,
            ]
        ),
        width=styles.KIT_PANEL_WIDTH,
        padding=styles.PANEL_PADDING,
        bgcolor=styles.BACKGROUND,
    )
