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


def build_kit_controls(controller: "BuildController") -> list[ft.Control]:
    if not controller.kit.items:
        return [ft.Text("No items packed yet!", italic=True)]

    controls: list[ft.Control] = []

    for item in controller.kit.items:
        catalogue_item = controller.get_catalogue_item(item.item_id)
        controls.append(
            ft.Row(
                controls=[
                    # TODO: replace item id with item name
                    ft.Text(f"{catalogue_item.name} x {item.qty}"),
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        on_click=handle_decrement(controller, item.item_id),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=handle_increment(controller, item.item_id),
                    ),
                    ft.TextButton(
                        "Remove", on_click=handle_remove(controller, item.item_id)
                    ),
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
