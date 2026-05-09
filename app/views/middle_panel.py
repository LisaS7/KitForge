import flet as ft

from app.views import styles


def build_middle_panel(controller: "BuildController") -> ft.Container:  # type: ignore  # noqa: F821
    bag_dropzone = ft.Container(
        width=280,
        height=360,
        border=ft.Border.all(styles.BORDER_WIDTH, styles.BORDER),
        content=ft.Column(
            controls=[
                ft.Image(
                    src="backpack.png",
                    width=200,
                    height=200,
                    fit="contain",  # type: ignore
                ),
                ft.Text("Drag items here", color=styles.MUTED_TEXT),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=styles.ITEM_SPACING,
        ),
    )

    return ft.Container(
        expand=True,
        bgcolor=styles.BACKGROUND,
        border=ft.border.only(
            right=ft.BorderSide(styles.BORDER_WIDTH, styles.BORDER),
        ),
        content=ft.Column(
            controls=[bag_dropzone],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
