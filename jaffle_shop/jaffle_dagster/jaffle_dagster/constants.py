import os
from pathlib import Path

from dagster_dbt import DbtCliResource


SENSOR_DIRECTORY = "../../sensor_demo/"
DBT_PROJECT_DIR = Path(__file__).joinpath("..", "..", "..").resolve()

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt = DbtCliResource(project_dir=os.fspath(DBT_PROJECT_DIR))
    dbt_parse_invocation = dbt.cli(["parse"]).wait()
    DBT_MANIFEST_PATH = dbt_parse_invocation.target_path.joinpath("manifest.json")
else:
    DBT_MANIFEST_PATH = DBT_PROJECT_DIR.joinpath("target", "manifest.json")
