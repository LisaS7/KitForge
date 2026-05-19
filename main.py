import logging

import flet as ft

from app.catalogue import group_by_category, load_catalogue, validate_catalogue
from app.config import KITS_DIR, LOG_FILE
from app.controllers.app_controller import AppController
from app.models import Kit, KitConfig
from app.storage import load_all_kits
from app.views.common.page import configure_page
from app.views.error_screen import error_screen

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

    try:
        data = load_catalogue()
    except Exception as e:
        logging.exception("Failed to load catalogue")
        page.add(error_screen([str(e)]))
        return

    catalogue_errors = validate_catalogue(data)

    if catalogue_errors:
        for error in catalogue_errors:
            logging.error(error)
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(error_screen(catalogue_errors))
        return

    categories = group_by_category(data)
    catalogue_lookup = {item.id: item for item in data}

    kit_config = KitConfig(
        weight_limit_g=25000,
        num_adults=2,
        num_children=0,
        num_young_children=0,
        num_infants=0,
        duration_days=10,
    )

    kits = load_all_kits(KITS_DIR)
    if not kits:
        kits = [Kit.create("My Kit", kit_config)]

    controller = AppController(page, kits, categories, catalogue_lookup)

    # controller.show_build_screen(kit)
    controller.show_kit_list()


if __name__ == "__main__":
    ft.run(
        main=main,
        assets_dir="assets",
    )
