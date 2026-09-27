"""Main application window for VehicleLog."""

import flet as ft


def create_main_window(page: ft.Page) -> None:
    """Configure and display the main VehicleLog window."""

    page.title = "VehicleLog"
    page.window.width = 900
    page.window.height = 600

    title = ft.Text(
        "VehicleLog",
        size=32,
        weight=ft.FontWeight.BOLD,
    )

    subtitle = ft.Text(
        "Personal Vehicle Maintenance Tracker",
        size=16,
    )

    garage_message = ft.Text(
        "Your garage is currently empty.",
        size=20,
    )

    page.add(
        ft.Column(
            controls=[
                title,
                subtitle,
                ft.Divider(),
                garage_message,
            ],
            spacing=15,
        )
    )