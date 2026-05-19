from typing import TYPE_CHECKING

import flet as ft

if TYPE_CHECKING:
    from app.controllers.app_controller import AppController


def build_kit_list_screen(controller: "AppController") -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Kit List"),
            *[
                ft.Button(
                    kit.name,
                    on_click=lambda _, k=kit: controller.show_build_screen(k),
                )
                for kit in controller.kits
            ],
        ]
    )
