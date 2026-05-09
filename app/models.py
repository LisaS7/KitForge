import datetime as dt
import uuid
from enum import StrEnum

from pydantic import BaseModel, Field, model_validator


class Category(StrEnum):
    WATER = "Water"
    FOOD = "Food"
    MEDICAL = "Medical"
    LIGHT = "Light"
    FIRE = "Fire"
    SHELTER = "Shelter"
    TOOLS = "Tools"
    NAVIGATION = "Navigation"
    HYGIENE = "Hygiene"
    COMMUNICATION = "Communication"
    DOCUMENTS = "Documents"


class RequirementType(StrEnum):
    ITEM = "item"
    CATEGORY = "category"
    RESOURCE = "resource"


class ResourceType(StrEnum):
    WATER_SOURCE = "water_source"
    WATER_ML = "water_ml"


class Requirement(BaseModel):
    type: RequirementType
    target_id: str | None = None
    target_category: Category | None = None
    resource: ResourceType | None = None
    amount: int | None = None
    exclude_self: bool = False


class CatalogueItem(BaseModel):
    id: str
    name: str
    category: Category
    weight_g: int = Field(ge=0)
    calories: int = Field(ge=0)
    water_ml: int = Field(ge=0)
    water_purification_ml: int = Field(ge=0)
    default_qty: int = Field(ge=1)
    notes: str | None = None
    requires: list[Requirement] = Field(default_factory=list)


class KitConfig(BaseModel):
    weight_limit_g: int = Field(gt=0)
    num_adults: int = Field(ge=0)
    num_children: int = Field(ge=0)
    num_young_children: int = Field(ge=0)
    num_infants: int = Field(ge=0)
    duration_days: int = Field(ge=1)

    @model_validator(mode="after")
    def at_least_one_person(self) -> "KitConfig":
        total = (
            self.num_adults
            + self.num_children
            + self.num_young_children
            + self.num_infants
        )
        if total < 1:
            raise ValueError("Kit must have at least one person")
        return self


class KitItem(BaseModel):
    item_id: str
    qty: int = Field(ge=1)


class Kit(BaseModel):
    id: str
    name: str
    created_at: dt.datetime
    modified_at: dt.datetime
    config: KitConfig
    items: list[KitItem] = Field(default_factory=list)

    @classmethod
    def create(cls, name: str, config: KitConfig):
        now = dt.datetime.now(dt.timezone.utc)
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            created_at=now,
            modified_at=now,
            config=config,
        )

    def add_item(self, item_id: str):
        existing = next((i for i in self.items if i.item_id == item_id), None)

        if existing:
            existing.qty += 1
        else:
            self.items.append(KitItem(item_id=item_id, qty=1))

        self.modified_at = dt.datetime.now(dt.timezone.utc)

    def remove_item(self, item_id: str):
        self.items = [item for item in self.items if item.item_id != item_id]
        self.modified_at = dt.datetime.now(dt.timezone.utc)

    def increment_item(self, item_id: str):
        existing = next((i for i in self.items if i.item_id == item_id), None)

        if not existing:
            return

        existing.qty += 1
        self.modified_at = dt.datetime.now(dt.timezone.utc)

    def decrement_item(self, item_id: str):
        existing = next((i for i in self.items if i.item_id == item_id), None)

        if not existing:
            return

        if existing.qty > 1:
            existing.qty -= 1
        else:
            self.items = [item for item in self.items if item.item_id != item_id]

        self.modified_at = dt.datetime.now(dt.timezone.utc)
