import flet as ft

from app.views import styles


def configure_page(page: ft.Page) -> None:
    page.title = "KitForge"
    page.window_width = 1200
    page.window_height = 800
    page.padding = styles.PAGE_PADDING
    page.bgcolor = styles.BACKGROUND
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            on_surface=styles.TEXT,
            primary=styles.PRIMARY,
            on_primary="#ffffff",
            error=styles.DANGER,
            surface=styles.SURFACE,
        ),
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=styles.TEXT, size=styles.BODY_SIZE),
            body_large=ft.TextStyle(color=styles.TEXT),
            title_large=ft.TextStyle(
                color=styles.TEXT, size=styles.TITLE_SIZE, weight=ft.FontWeight.BOLD
            ),
            title_medium=ft.TextStyle(
                color=styles.TEXT,
                size=styles.HEADER_TITLE_SIZE,
                weight=ft.FontWeight.BOLD,
            ),
            label_medium=ft.TextStyle(
                color=styles.TEXT, size=styles.LABEL_SIZE, weight=ft.FontWeight.BOLD
            ),
            label_small=ft.TextStyle(color=styles.MUTED_TEXT, size=10),
        ),
    )
