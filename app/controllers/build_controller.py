import threading

import flet as ft

from app.config import KITS_DIR
from app.models import CatalogueItem, Category, Kit
from app.stats import KitStats
from app.storage import save_kit
from app.views.build.catalogue_panel import build_category_grid, build_item_list
from app.views.build.kit_panel import build_kit_controls
from app.views.build.stats_panel import build_stats_controls


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
        self.collapsed_categories: set[Category] = set()

        self.catalogue_column: ft.Column | None = None
        self.kit_column: ft.Column | None = None
        self.bag_area: ft.Control | None = None
        self.stats_panel: ft.Control | None = None

        self._save_timer: threading.Timer | None = None

    def get_catalogue_item(self, item_id: str) -> CatalogueItem:
        return self.catalogue_lookup[item_id]

    def select_category(self, category: Category) -> None:
        self.selected_category = category
        self.refresh_catalogue()
        self.page.update()

    def clear_selected_category(self) -> None:
        self.selected_category = None
        self.refresh_catalogue()
        self.page.update()

    def toggle_category(self, category: Category) -> None:
        if category in self.collapsed_categories:
            self.collapsed_categories.remove(category)
        else:
            self.collapsed_categories.add(category)

        self.refresh_kit()
        self.page.update()

    def is_category_covered(self, category: Category) -> bool:
        return any(
            self.catalogue_lookup[kit_item.item_id].category == category
            for kit_item in self.kit.items
        )

    def add_item(self, item: CatalogueItem) -> None:
        self.kit.add_item(item.id)
        self.schedule_save()
        self.refresh_all()

    def remove_item(self, item_id: str) -> None:
        self.kit.remove_item(item_id)
        self.schedule_save()
        self.refresh_all()

    def increment_item(self, item_id: str) -> None:
        self.kit.increment_item(item_id)
        self.schedule_save()
        self.refresh_all()

    def decrement_item(self, item_id: str) -> None:
        self.kit.decrement_item(item_id)
        self.schedule_save()
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

    def save_now(self) -> None:
        if self._save_timer:
            self._save_timer.cancel()
            self._save_timer = None

        save_kit(self.kit, KITS_DIR)

    def schedule_save(self) -> None:
        if self._save_timer:
            self._save_timer.cancel()
        self._save_timer = threading.Timer(0.5, self.save_now)
        self._save_timer.daemon = True
        self._save_timer.start()
