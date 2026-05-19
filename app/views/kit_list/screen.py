from typing import TYPE_CHECKING

import flet as ft

from app.stats import KitStats
from app.views.common import styles

if TYPE_CHECKING:
    from app.controllers.app_controller import AppController


def _readiness_colour(score: int) -> str:
    if score >= 70:
        return styles.PRIMARY
    if score >= 40:
        return styles.WARNING
    return styles.DANGER


def _format_date(dt) -> str:
    return dt.strftime("%-d %b %Y")


def _kit_card(kit, stats: KitStats, controller: "AppController") -> ft.Container:
    kit_name = ft.Text(
        kit.name,
        size=styles.HEADER_TITLE_SIZE,
        weight=ft.FontWeight.BOLD,
        color=styles.TEXT,
    )
    score_colour = _readiness_colour(stats.readiness_score)
    readiness_score = [
        ft.Text(
            f"{stats.readiness_score}%",
            size=styles.PANEL_TITLE_SIZE,
            weight=ft.FontWeight.BOLD,
            color=score_colour,
        ),
        ft.Text(
            "READINESS",
            size=styles.LABEL_SIZE,
            color=styles.MUTED_TEXT,
            weight=ft.FontWeight.BOLD,
        ),
    ]

    kit_weight = ft.Row(
        controls=[
            ft.Text("Weight", size=styles.BODY_SIZE, color=styles.MUTED_TEXT),
            ft.Text(
                f"{stats.total_weight_kg():.1f} kg / {stats.weight_limit_kg():.0f} kg",
                size=styles.BODY_SIZE,
                color=styles.TEXT,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    last_modified = ft.Row(
        controls=[
            ft.Text("Last modified", size=styles.BODY_SIZE, color=styles.MUTED_TEXT),
            ft.Text(
                _format_date(kit.modified_at),
                size=styles.BODY_SIZE,
                color=styles.TEXT,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    body = ft.Container(
        content=ft.Column(
            controls=[
                kit_name,
                *readiness_score,
                ft.Column(
                    controls=[kit_weight, last_modified],
                    spacing=styles.ITEM_SPACING,
                ),
            ],
            spacing=styles.ITEM_SPACING,
        ),
        padding=ft.padding.all(styles.SECTION_SPACING),
        expand=True,
    )

    def action_btn(label: str, on_click, danger: bool = False) -> ft.TextButton:
        color = styles.TEXT
        return ft.TextButton(
            content=ft.Text(label, size=styles.BODY_SIZE, color=color),
            on_click=on_click,
            style=ft.ButtonStyle(
                padding=ft.padding.symmetric(vertical=styles.ITEM_SPACING),
                shape=ft.RoundedRectangleBorder(radius=0),
                overlay_color={
                    ft.ControlState.HOVERED: "#f5e0e0" if danger else styles.SURFACE,
                },
                color={ft.ControlState.HOVERED: styles.DANGER} if danger else None,
            ),
            expand=True,
        )

    footer = ft.Container(
        content=ft.Row(
            controls=[
                action_btn(
                    "✎ Edit", on_click=lambda _, k=kit: controller.show_build_screen(k)
                ),
                ft.VerticalDivider(width=1, color=styles.BORDER),
                action_btn("⧉ Copy", on_click=lambda _, k=kit: controller.copy_kit(k)),
                ft.VerticalDivider(width=1, color=styles.BORDER),
                action_btn(
                    "🗑 Delete",
                    on_click=lambda _, k=kit: controller.delete_kit(k),
                    danger=True,
                ),
            ],
            spacing=0,
        ),
        border=ft.border.only(top=ft.BorderSide(1, styles.BORDER)),
    )

    return ft.Container(
        content=ft.Column(controls=[body, footer], spacing=0),
        border=ft.border.all(styles.BORDER_WIDTH, styles.TEXT),
        bgcolor=styles.BACKGROUND,
        on_hover=lambda e: setattr(
            e.control,
            "bgcolor",
            styles.ACCENT if e.data == "true" else styles.BACKGROUND,
        )
        or e.control.update(),
        expand=True,
    )


def _empty_state() -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("🎒", size=styles.TITLE_SIZE, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "You don't have any kits yet.",
                    size=styles.BODY_SIZE,
                    color=styles.MUTED_TEXT,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Click + New Kit to get started.",
                    size=styles.BODY_SIZE,
                    color=styles.MUTED_TEXT,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=styles.ITEM_SPACING,
        ),
        padding=ft.padding.symmetric(vertical=80),
        alignment=ft.Alignment.CENTER,
    )


def build_kit_list_screen(controller: "AppController") -> ft.Control:
    # Header
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "KitForge",
                    size=styles.PANEL_TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                    color=styles.TEXT,
                ),
                ft.Text(
                    "Emergency Kit Planner",
                    size=styles.BODY_SIZE,
                    color=styles.MUTED_TEXT,
                ),
                ft.Container(expand=True),
                ft.ElevatedButton(
                    "+ New Kit",
                    on_click=lambda _: controller.new_kit(),
                    bgcolor=styles.PRIMARY,
                    color=styles.ACCENT,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=0),
                        side=ft.BorderSide(0),
                        padding=ft.padding.symmetric(
                            horizontal=styles.SECTION_SPACING, vertical=6
                        ),
                    ),
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=ft.padding.symmetric(
            horizontal=styles.PAGE_PADDING, vertical=styles.PAGE_PADDING
        ),
        border=ft.border.only(bottom=ft.BorderSide(styles.BORDER_WIDTH, styles.TEXT)),
        bgcolor=styles.ACCENT,
    )

    # Kit grid or empty state
    if controller.kits:
        cards = [
            _kit_card(
                kit,
                KitStats.calculate_stats(kit, controller.catalogue_lookup),
                controller,
            )
            for kit in controller.kits
        ]
        # Arrange into rows of 3
        rows = []
        for i in range(0, len(cards), 3):
            chunk = cards[i : i + 3]
            # Pad with invisible spacers so the last row aligns left
            while len(chunk) < 3:
                chunk.append(ft.Container(expand=True))
            rows.append(
                ft.Row(
                    controls=chunk,  # pyright: ignore[reportArgumentType]
                    spacing=styles.SECTION_SPACING,
                    expand=True,
                )
            )

        grid = ft.Column(controls=rows, spacing=styles.SECTION_SPACING)
        body_content = ft.Column(
            controls=[
                ft.Text(
                    "YOUR KITS",
                    size=styles.BODY_SIZE,
                    weight=ft.FontWeight.BOLD,
                    color=styles.MUTED_TEXT,
                ),
                grid,
            ],
            spacing=styles.SECTION_SPACING,
        )
    else:
        body_content = _empty_state()

    content = ft.Container(
        content=body_content,
        padding=ft.padding.symmetric(
            horizontal=styles.PAGE_PADDING, vertical=styles.PAGE_PADDING
        ),
        expand=True,
    )

    return ft.Column(
        controls=[header, content],
        spacing=0,
        expand=True,
    )
