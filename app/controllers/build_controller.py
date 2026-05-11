import flet as ft

from app.models import CatalogueItem, Category, Kit
from app.stats import KitStats
from app.views.catalogue_panel import build_category_grid, build_item_list
from app.views.kit_panel import build_kit_controls
from app.views.stats_panel import build_stats_controls


class BuildController:
    def __init__(
        self,
        page: ft.Page,
        kit: Kit,
        categories: dict[Category, list[CatalogueItem]],
        catalogue_lookup: dict[str, CatalogueItem],
    ):
        self.page = page
        self.kit = kit
        self.categories = categories
        self.catalogue_lookup = catalogue_lookup
        self.selected_category: Category | None = None

        self.catalogue_column: ft.Column | None = None
        self.kit_column: ft.Column | None = None
        self.bag_area: ft.Control | None = None
        self.stats_panel: ft.Control | None = None

    def select_category(self, category: Category) -> None:
        self.selected_category = category
        self.refresh_catalogue()
        self.page.update()

    def clear_selected_category(self) -> None:
        self.selected_category = None
        self.refresh_catalogue()
        self.page.update()

    def add_item(self, item: CatalogueItem) -> None:
        self.kit.add_item(item.id)
        self.refresh_all()

    def remove_item(self, item_id: str) -> None:
        self.kit.remove_item(item_id)
        self.refresh_all()

    def increment_item(self, item_id: str) -> None:
        self.kit.increment_item(item_id)
        self.refresh_all()

    def decrement_item(self, item_id: str) -> None:
        self.kit.decrement_item(item_id)
        self.refresh_all()

    def refresh_catalogue(self) -> None:
        if self.catalogue_column is None:
            return

        if self.selected_category is None:
            self.catalogue_column.controls = [build_category_grid(self)]
        else:
            self.catalogue_column.controls = [
                build_item_list(self, self.selected_category)
            ]

    def refresh_kit(self) -> None:
        if self.kit_column is None:
            return
        self.kit_column.controls = build_kit_controls(self)

    def refresh_stats(self) -> None:
        if self.stats_panel is None:
            return
        stats = KitStats.calculate_stats(self.kit, self.catalogue_lookup)
        self.stats_panel.content.controls = build_stats_controls(stats)  # type: ignore

    def refresh_all(self) -> None:
        self.refresh_catalogue()
        self.refresh_kit()
        self.refresh_stats()
        self.page.update()
