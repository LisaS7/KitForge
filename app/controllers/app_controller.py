import flet as ft

from app.controllers.build_controller import BuildController
from app.models import CatalogueItem, Category, Kit
from app.views.build.screen import build_screen
from app.views.kit_list.screen import build_kit_list_screen


class AppController:
    def __init__(
        self,
        page: ft.Page,
        kits: list[Kit],
        categories: dict[Category, list[CatalogueItem]],
        catalogue_lookup: dict[str, CatalogueItem],
    ):
        self.page = page
        self.kits = kits
        self.current_kit: Kit | None = None

        self.categories = categories
        self.catalogue_lookup = catalogue_lookup

    def show_kit_list(self):
        view = build_kit_list_screen(self)
        self.page.controls.clear()
        self.page.add(view)
        self.page.update()

    def show_build_screen(self, kit: Kit):
        self.current_kit = kit

        controller = BuildController(
            self.page, kit, self.categories, self.catalogue_lookup
        )

        build_view = build_screen(controller)

        self.page.controls.clear()
        self.page.add(build_view)
        self.page.update()

    def show_report(self, kit: Kit):
        pass
