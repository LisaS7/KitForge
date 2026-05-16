from dataclasses import dataclass

from app.models import CatalogueItem, Kit


@dataclass(slots=True)
class KitStats:
    total_calories: int
    calorie_requirement: int

    stored_water_ml: int
    purifiable_water_ml: int
    water_requirement_ml: int

    total_weight_g: int
    weight_limit_g: int
    weight_percentage: float
    weight_bar_colour: str

    readiness_score: int

    def total_weight_kg(self) -> float:
        return self.total_weight_g / 1000

    def weight_limit_kg(self) -> float:
        return self.weight_limit_g / 1000

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

        weight_percentage = total_weight_g / kit.config.weight_limit_g
        if weight_percentage < 0.75:
            weight_bar_colour = "green"
        elif weight_percentage < 1:
            weight_bar_colour = "amber"
        else:
            weight_bar_colour = "red"

        return cls(
            total_weight_g=total_weight_g,
            total_calories=total_calories,
            stored_water_ml=stored_water_ml,
            purifiable_water_ml=purifiable_water_ml,
            calorie_requirement=0,
            water_requirement_ml=0,
            weight_limit_g=kit.config.weight_limit_g,
            readiness_score=0,
            weight_percentage=weight_percentage,
            weight_bar_colour=weight_bar_colour,
        )
