from dataclasses import dataclass

from app.models import CatalogueItem, Kit
from app.views.common import styles

ADULT_CALORIES_PER_DAY = 2000
CHILD_CALORIES_PER_DAY = 1500
YOUNG_CHILD_CALORIES_PER_DAY = 1200
INFANT_CALORIES_PER_DAY = 700

ADULT_WATER_ML_PER_DAY = 3000
CHILD_WATER_ML_PER_DAY = 2000
YOUNG_CHILD_WATER_ML_PER_DAY = 1500
INFANT_WATER_ML_PER_DAY = 1000


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

    def stored_water_l(self) -> float:
        return self.stored_water_ml / 1000

    def water_requirement_l(self) -> float:
        return self.water_requirement_ml / 1000

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
            weight_bar_colour = styles.SUCCESS
        elif weight_percentage < 1:
            weight_bar_colour = styles.WARNING
        else:
            weight_bar_colour = styles.DANGER

        daily_calories = (
            kit.config.num_adults * ADULT_CALORIES_PER_DAY
            + kit.config.num_children * CHILD_CALORIES_PER_DAY
            + kit.config.num_young_children * YOUNG_CHILD_CALORIES_PER_DAY
            + kit.config.num_infants * INFANT_CALORIES_PER_DAY
        )

        daily_water_ml = (
            kit.config.num_adults * ADULT_WATER_ML_PER_DAY
            + kit.config.num_children * CHILD_WATER_ML_PER_DAY
            + kit.config.num_young_children * YOUNG_CHILD_WATER_ML_PER_DAY
            + kit.config.num_infants * INFANT_WATER_ML_PER_DAY
        )

        calorie_requirement = daily_calories * kit.config.duration_days
        water_requirement_ml = daily_water_ml * kit.config.duration_days

        return cls(
            total_weight_g=total_weight_g,
            total_calories=total_calories,
            stored_water_ml=stored_water_ml,
            purifiable_water_ml=purifiable_water_ml,
            calorie_requirement=calorie_requirement,
            water_requirement_ml=water_requirement_ml,
            weight_limit_g=kit.config.weight_limit_g,
            readiness_score=0,
            weight_percentage=weight_percentage,
            weight_bar_colour=weight_bar_colour,
        )
