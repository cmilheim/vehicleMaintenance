# VehicleLog

VehicleLog is a personal vehicle maintenance tracking application. It is an early-stage desktop app built with Python and Flet.

## Current Status

The app currently opens a VehicleLog window with a welcome heading and an empty-garage message. Vehicle records, maintenance logging, and database persistence are not implemented yet. The `data/` directory and test suite are currently empty.

## Requirements

- Python 3.11 or newer

## Setup

From the repository root, create and activate a virtual environment, then install the project and its dependencies:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run

Start the application from the repository root:

```powershell
python -m vehiclelog
```

## Project Layout

```text
src/vehiclelog/
	app.py                 Application startup
	database/              Database module (not implemented yet)
	models/                Vehicle model (not implemented yet)
	ui/main_window.py      Main Flet window
tests/                   Automated tests (not added yet)
data/                    Reserved for application data
```
