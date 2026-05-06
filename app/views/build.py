import flet as ft


def build_header():
    return ft.Column(
        [
            ft.Text("KitForge", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Emergency kit planner"),
        ]
    )


def build_catalogue(categories):

    grouped_catalogue_items: list[ft.Control] = []
    for category, items in categories.items():
        grouped_catalogue_items.append(
            ft.Text(category, size=20, weight=ft.FontWeight.BOLD)
        )

        for item in items[:3]:
            grouped_catalogue_items.append(
                ft.Text(f"- {item['name']}", color="#2e2e2e")
            )

    return ft.Container(
        content=ft.Column(
            controls=[ft.Text("Catalogue", size=24, weight=ft.FontWeight.BOLD)]
            + grouped_catalogue_items,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=2,
    )


def build_kit_panel():
    return ft.Container(
        content=ft.Column([ft.Text("Kit List"), ft.Text("No items packed yet!")]),
        expand=1,
    )


def build_screen(categories):
    header = build_header()
    catalogue_panel = build_catalogue(categories)
    kit_panel = build_kit_panel()

    main_content = ft.Row(
        controls=[catalogue_panel, kit_panel], expand=True, spacing=16
    )

    return ft.Column(controls=[header, main_content], expand=True)
