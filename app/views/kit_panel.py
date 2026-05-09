import flet as ft

from app.views import styles


def handle_increment(controller: "BuildController", item_id: str):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.increment_item(item_id)

    return on_click


def handle_decrement(controller: "BuildController", item_id: str):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.decrement_item(item_id)

    return on_click


def handle_remove(controller: "BuildController", item_id: str):  # type: ignore  # noqa: F821
    def on_click(e):
        controller.remove_item(item_id)

    return on_click


def build_kit_controls(controller: "BuildController") -> list[ft.Control]:  # type: ignore  # noqa: F821
    kit = controller.kit
    if not kit.items:
        return [ft.Text("No items packed yet!", italic=True)]

    controls: list[ft.Control] = []

    for item in kit.items:
        controls.append(
            ft.Row(
                controls=[
                    ft.Text(f"{item.item_id} x {item.qty}"),
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        on_click=handle_decrement(controller, item.item_id),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=handle_increment(controller, item.item_id),
                    ),
                    ft.TextButton("Remove", on_click=handle_remove(controller, item.item_id)),  # type: ignore
                ]
            )
        )

    return controls


def build_kit_panel(controller: "BuildController") -> ft.Control:  # type: ignore  # noqa: F821
    controller.kit_column = ft.Column(build_kit_controls(controller))

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Kit List",
                    size=styles.PANEL_TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                ),
                controller.kit_column,
            ]
        ),
        expand=1,
    )
