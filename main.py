import logging

import flet as ft

from app.catalogue import group_by_category, load_catalogue
from app.config import LOG_FILE
from app.models import Kit, KitConfig
from app.views.build import build_screen
from app.views.page import configure_page

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
    ],
)

logging.getLogger("flet").setLevel(logging.WARNING)
logging.getLogger("flet_desktop").setLevel(logging.WARNING)
logging.getLogger("flet_transport").setLevel(logging.WARNING)
logging.getLogger("flet_controls").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)


def main(page: ft.Page) -> None:
    configure_page(page)

    data = load_catalogue()
    categories = group_by_category(data)

    kit_config = KitConfig(
        weight_limit_g=25000,
        num_adults=2,
        num_children=0,
        num_young_children=0,
        num_infants=0,
        duration_days=10,
    )
    kit = Kit.create("Test Kit", kit_config)

    build_view = build_screen(page, categories, kit)

    page.add(build_view)


if __name__ == "__main__":
    ft.run(main=main)
