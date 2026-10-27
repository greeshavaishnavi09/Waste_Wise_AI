
import logging
import argparse
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
)

PROJECT_NAME = "WasteWise-AI"

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
            "api": {
                "v1": {
                    "auth.py": None,
                    "dashboard.py": None,
                    "products.py": None,
                    "batches.py": None,
                    "sales.py": None,
                    "forecasts.py": None,
                    "risk.py": None,
                    "recommendations.py": None,
                    "waste.py": None,
                }
            },
            "core": {
                "config.py": None,
                "security.py": None,
            },
            "db": {
                "session.py": None,
                "base.py": None,
            },
            "models": {
                "user.py": None,
                "product.py": None,
                "inventory.py": None,
                "sales.py": None,
                "prediction.py": None,
            },
            "schemas": {},
            "repositories": {},
            "services": {
                "inventory_service.py": None,
                "forecast_service.py": None,
                "recommendation_service.py": None,
            },
            "main.py": None,
            "dependencies.py": None,
        },
        "tests": {},
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
            "06_model_evaluation.ipynb": None,
        },
        "src": {
            "data_validation.py": None,
            "preprocessing.py": None,
            "feature_engineering.py": None,
            "train_forecast.py": None,
            "train_expiry_risk.py": None,
            "train_models.py": None,
            "evaluate.py": None,
            "predict.py": None,
        },
        "experiments": {},
        "artifacts": {},
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
    """Create directories and empty files recursively."""

    for name, content in structure.items():
        path = base_path / name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)

        elif content is None:
            path.parent.mkdir(parents=True, exist_ok=True)

            if not path.exists():
                path.touch()
                logging.info("Created file: %s", path)
            else:
                logging.info("Skipped existing file: %s", path)


def main():
    parser = argparse.ArgumentParser(
        description="Create the WasteWise-AI project structure."
    )

    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Parent directory for the project.",
    )

    args = parser.parse_args()
    parent_path = args.path.expanduser().resolve()
    project_root = parent_path / PROJECT_NAME

    project_root.mkdir(parents=True, exist_ok=True)

    create_structure(project_root, PROJECT_STRUCTURE)

    logging.info("Project structure created at: %s", project_root)
    logging.info("Empty files were created where files did not already exist.")


if __name__ == "__main__":
    main()
