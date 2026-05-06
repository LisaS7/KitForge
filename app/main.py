import flet as ft
from catalogue import group_by_category, load_json
from views.build import build_screen


def main(page: ft.Page):
    page.title = "KitForge"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 24

    data = load_json()
    categories = group_by_category(data)

    build_view = build_screen(categories)

    page.add(build_view)


if __name__ == "__main__":
    ft.run(main=main)
