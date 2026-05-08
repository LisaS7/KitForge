import flet as ft

from app.models import CatalogueItem, Category, Kit
from app.views.kit_panel import build_kit_controls


class BuildController:
    def __init__(
        self, page: ft.Page, kit: Kit, categories: dict[Category, list[CatalogueItem]]
    ):
        self.page = page
        self.kit = kit
        self.categories = categories
        self.selected_category: Category | None = None

        self.catalogue_column: ft.Column | None = None
        self.kit_column: ft.Column | None = None
        self.bag_area: ft.Control | None = None

    def select_category(self, category: Category) -> None:
        self.selected_category = category
        # TODO: finish logic later

    def add_item(self, item: CatalogueItem) -> None:
        self.kit.add_item(item.id)
        self.refresh_kit()
        self.page.update()

    def remove_item(self, item_id: str) -> None:
        pass

    def increment_item(self, item_id: str) -> None:
        pass

    def decrement_item(self, item_id: str) -> None:
        pass

    def refresh_catalogue(self) -> None:
        pass

    def refresh_kit(self) -> None:
        if self.kit_column is None:
            return
        self.kit_column.controls = build_kit_controls(self.kit)

    def refresh_stats(self) -> None:
        pass

    def refresh_all(self) -> None:
        self.refresh_catalogue()
        self.refresh_kit()
        self.refresh_stats()
        self.page.update()
