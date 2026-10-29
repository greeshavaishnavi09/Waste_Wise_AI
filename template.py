
import argparse
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
)

# The existing project root is the folder containing this script.
DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent

# Folder structure: directories use dictionaries; files use None.
PROJECT_STRUCTURE = {
    "frontend": {
        "public": {},
        "src": {
            "assets": {},
            "components": {
                "common": {},
                "charts": {},
                "tables": {},
                "forms": {},
            },
            "layouts": {
                "MainLayout.tsx": None,
                "AuthLayout.tsx": None,
            },
            "pages": {
                "Landing.tsx": None,
                "Login.tsx": None,
                "Register.tsx": None,
                "Dashboard.tsx": None,
                "Products.tsx": None,
                "Inventory.tsx": None,
                "SalesHistory.tsx": None,
                "DemandForecast.tsx": None,
                "ExpiryRisk.tsx": None,
                "Recommendations.tsx": None,
                "WasteReports.tsx": None,
                "ModelMetrics.tsx": None,
            },
            "services": {
                "api.ts": None,
                "auth.ts": None,
                "products.ts": None,
                "inventory.ts": None,
                "predictions.ts": None,
            },
            "hooks": {},
            "types": {},
            "utils": {},
            "App.tsx": None,
            "main.tsx": None,
        },
        "package.json": None,
        "vite.config.ts": None,
        "tsconfig.json": None,
        "index.html": None,
    },
    "backend": {
        "app": {
            "__init__.py": None,
            "api": {
                "__init__.py": None,
                "v1": {
                    "__init__.py": None,
                    "auth.py": None,
                    "dashboard.py": None,
                    "products.py": None,
                    "batches.py": None,
                    "sales.py": None,
                    "forecasts.py": None,
                    "risk.py": None,
                    "recommendations.py": None,
                    "waste.py": None,
                    "metrics.py": None,
                },
            },
            "core": {
                "__init__.py": None,
                "config.py": None,
                "security.py": None,
            },
            "db": {
                "__init__.py": None,
                "session.py": None,
                "base.py": None,
            },
            "models": {
                "__init__.py": None,
                "user.py": None,
                "product.py": None,
                "inventory.py": None,
                "sales.py": None,
                "prediction.py": None,
            },
            "schemas": {
                "__init__.py": None,
                "auth.py": None,
                "product.py": None,
                "inventory.py": None,
                "prediction.py": None,
            },
            "repositories": {
                "__init__.py": None,
            },
            "services": {
                "__init__.py": None,
                "inventory_service.py": None,
                "forecast_service.py": None,
                "recommendation_service.py": None,
            },
            "main.py": None,
            "dependencies.py": None,
        },
        "tests": {
            "__init__.py": None,
            "test_health.py": None,
            "test_auth.py": None,
            "test_predictions.py": None,
        },
        "requirements.txt": None,
        ".env.example": None,
    },
    "ml": {
        "data": {
            "raw": {},
            "interim": {},
            "processed": {},
        },
        "notebooks": {
            "01_data_understanding.ipynb": None,
            "02_eda.ipynb": None,
            "03_feature_engineering.ipynb": None,
            "04_demand_forecasting.ipynb": None,
            "05_expiry_risk_model.ipynb": None,
            "06_food_waste_model.ipynb": None,
            "07_discount_model.ipynb": None,
        },
        "src": {
            "__init__.py": None,
            "data_validation.py": None,
            "preprocessing.py": None,
            "feature_engineering.py": None,
            "train_forecast.py": None,
            "train_expiry_risk.py": None,
            "train_waste_model.py": None,
            "train_discount_model.py": None,
            "train_models.py": None,
            "evaluate.py": None,
            "predict.py": None,
            "inventory_optimizer.py": None,
            "model_utils.py": None,
        },
        "experiments": {},
        "artifacts": {},
        "reports": {},
        "tests": {},
        "requirements.txt": None,
    },
    "database": {
        "schema.sql": None,
        "seed_data.sql": None,
        "migrations": {},
    },
    "scripts": {
        "import_dataset.py": None,
        "generate_demo_data.py": None,
        "validate_data.py": None,
    },
    "docs": {
        "project_report.md": None,
        "api_documentation.md": None,
        "database_design.md": None,
        "model_card.md": None,
    },
    ".github": {
        "workflows": {
            "ci.yml": None,
        },
    },
    "tests": {},
    "docker-compose.yml": None,
    "Dockerfile": None,
    ".gitignore": None,
    ".env.example": None,
    "README.md": None,
}


def create_structure(base_path: Path, structure: dict) -> None:
    """Create missing directories and files without overwriting existing files."""

    for name, content in structure.items():
        path = base_path / name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)

        elif content is None:
            path.parent.mkdir(parents=True, exist_ok=True)

            if path.exists():
                logging.info("Preserved existing file: %s", path)
                continue

            # A notebook must contain valid notebook JSON,
            # not be a zero-byte empty file.
            if path.suffix == ".ipynb":
                notebook = {
                    "cells": [],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 5,
                }
                path.write_text(
                    json.dumps(notebook, indent=2),
                    encoding="utf-8",
                )
            else:
                path.touch()

            logging.info("Created file: %s", path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create missing WasteWise-AI project files."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=(
            "Existing project root. Defaults to the directory "
            "containing template.py."
        ),
    )
    args = parser.parse_args()

    project_root = args.path.expanduser().resolve()

    if not project_root.exists():
        parser.error(f"Project directory does not exist: {project_root}")

    if not project_root.is_dir():
        parser.error(f"Path is not a directory: {project_root}")

    logging.info("Project root: %s", project_root)
    create_structure(project_root, PROJECT_STRUCTURE)

    logging.info("Folder structure check completed.")
    logging.info(
        "Existing files were preserved. Newly created files may be empty."
    )
    logging.info(
        "Next: implement missing code and validate it before running the app."
    )


if __name__ == "__main__":
    main()
