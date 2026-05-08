import logging

import flet as ft

from app.catalogue import group_by_category, load_catalogue
from app.views.build import build_screen
from app.views.page import configure_page

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)


def main(page: ft.Page) -> None:
    configure_page(page)

    data = load_catalogue()
    categories = group_by_category(data)

    build_view = build_screen(categories)

    page.add(build_view)


if __name__ == "__main__":
    ft.run(main=main)
