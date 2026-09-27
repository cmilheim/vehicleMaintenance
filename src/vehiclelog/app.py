"""Main application module for VehicleLog."""

import flet as ft

from vehiclelog.ui.main_window import create_main_window


def main() -> None:
    """Start the VehicleLog application."""

    ft.run(create_main_window)