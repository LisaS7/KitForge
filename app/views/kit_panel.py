import flet as ft

from app.views import styles

from ..models import Kit


def build_kit_controls(kit: Kit) -> list[ft.Control]:
    if not kit.items:
        return [ft.Text("No items packed yet!", italic=True)]
    return [ft.Text(f"{item.item_id} x {item.qty}") for item in kit.items]


def build_kit_panel(controller: "BuildController") -> ft.Control:  # type: ignore  # noqa: F821
    controller.kit_column = ft.Column(build_kit_controls(controller.kit))

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
