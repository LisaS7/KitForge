from dataclasses import dataclass

from app.models import CatalogueItem, Kit


@dataclass(slots=True)
class KitStats:
    total_weight_g: int
    total_calories: int
    stored_water_ml: int
    purifiable_water_ml: int
    calorie_requirement: int
    water_requirement_ml: int
    weight_limit_g: int
    readiness_score: int

    @classmethod
    def calculate_stats(
        cls, kit: Kit, catalogue: dict[str, CatalogueItem]
    ) -> "KitStats":
        total_weight_g = 0
        total_calories = 0
        stored_water_ml = 0
        purifiable_water_ml = 0

        for kit_item in kit.items:
            catalogue_item = catalogue[kit_item.item_id]
            qty = kit_item.qty

            total_weight_g += catalogue_item.weight_g * qty
            total_calories += catalogue_item.calories * qty
            stored_water_ml += catalogue_item.water_ml * qty
            purifiable_water_ml += catalogue_item.water_purification_ml * qty

        return cls(
            total_weight_g=total_weight_g,
            total_calories=total_calories,
            stored_water_ml=stored_water_ml,
            purifiable_water_ml=purifiable_water_ml,
            calorie_requirement=0,
            water_requirement_ml=0,
            weight_limit_g=kit.config.weight_limit_g,
            readiness_score=0,
        )
