import flet as ft

from app.views import styles


def build_middle_panel(controller: "BuildController") -> ft.Container:  # type: ignore  # noqa: F821

    return ft.Container(
        expand=2,
        bgcolor=styles.BACKGROUND,
        content=ft.Column(
            controls=[
                ft.Image(
                    src="backpack.png",
                    width=200,
                    height=200,
                    fit="contain",
                ),
                ft.Text("Drag items here", color=styles.MUTED_TEXT),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
