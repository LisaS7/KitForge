import flet as ft

from app.models import Category

CATEGORY_ICONS = {
    Category.WATER: ft.Icons.WATER_DROP,
    Category.FOOD: ft.Icons.RESTAURANT,
    Category.MEDICAL: ft.Icons.MEDICAL_SERVICES,
    Category.LIGHT: ft.Icons.FLASHLIGHT_ON,
    Category.FIRE: ft.Icons.LOCAL_FIRE_DEPARTMENT,
    Category.SHELTER: ft.Icons.COTTAGE,
    Category.TOOLS: ft.Icons.HANDYMAN,
    Category.NAVIGATION: ft.Icons.EXPLORE,
    Category.HYGIENE: ft.Icons.SOAP,
    Category.COMMUNICATION: ft.Icons.CELL_TOWER,
    Category.DOCUMENTS: ft.Icons.DESCRIPTION,
}
