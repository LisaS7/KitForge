import flet as ft

from app.views.common import styles


def error_screen(errors: list[str]) -> ft.Control:
    error_items = [
        ft.Text(f"• {e}", color=styles.DANGER, size=styles.BODY_SIZE) for e in errors
    ]

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "⚠ Catalogue failed to load",
                size=styles.PANEL_TITLE_SIZE,
                weight=ft.FontWeight.BOLD,
                color=styles.TEXT,
            ),
            ft.Container(height=4),
            ft.Text(
                "Fix the errors below in catalogue.json and restart.",
                size=styles.BODY_SIZE,
                color=styles.MUTED_TEXT,
            ),
            ft.Container(height=16),
            ft.Container(
                width=520,
                bgcolor=styles.SURFACE,
                border=ft.border.all(styles.BORDER_WIDTH, styles.BORDER),
                border_radius=8,
                padding=16,
                content=ft.Column(controls=error_items, spacing=6, tight=True),  # type: ignore
            ),
        ],
    )
