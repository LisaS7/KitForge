# KitForge

A desktop application for planning emergency preparedness kits. Build a well-rounded bug-out bag by selecting items from a curated catalogue, tracking weight and nutritional coverage, and generating a readiness report that identifies gaps.

## Features

- **Kit Management** — Create, rename, copy, and delete multiple named kits
- **Weight Tracking** — Set weight limits and monitor capacity with a visual indicator
- **Item Catalogue** — Browse 11 categories of emergency preparedness items
- **Readiness Scoring** — Get a 0–100% score based on category coverage
- **Gap Analysis** — Identify missing critical categories and unmet item dependencies
- **Local-First** — All data stays on your machine; fully offline

## Requirements

- Python 3.12+
- Linux (primary platform; Windows/macOS not tested)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd KitForge

# Install dependencies with uv
uv sync

# Run the application
uv run python main.py
```

## Project Structure

```
KitForge/
├── data/
│   └── catalogue.json      # Item catalogue
├── docs/                   # Design documents and wireframes
├── main.py                 # Application entry point
└── pyproject.toml          # Project configuration
```

## Development

```bash
# Run tests
uv run pytest

# Activate virtual environment
source .venv/bin/activate
```

## Documentation

- [Product Requirements Document](docs/PRD.md)
- [Functional Requirements Document](docs/FRD.md)
- [User Stories](docs/user-stories.md)
- [Data Model](docs/data-model.md)
- [Data Flow](docs/data-flow.md)
