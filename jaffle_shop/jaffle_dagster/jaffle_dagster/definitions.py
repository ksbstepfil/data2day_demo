import os

from dagster import Definitions, EnvVar, load_assets_from_modules
from dagster_dbt import DbtCliResource
from dagster_snowflake_pandas import SnowflakePandasIOManager

from . import assets
from .constants import DBT_PROJECT_DIR, SENSOR_DIRECTORY
from .schedules import schedules
from .sensors import my_directory_sensor
from .resources import PandasParquetIOManager

defs = Definitions(
    assets=load_assets_from_modules([assets]),
    schedules=schedules,
    sensors=[my_directory_sensor],
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(DBT_PROJECT_DIR)),
        "snowflake_io_manager": SnowflakePandasIOManager(
            account="xskqzat-bk95941",
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            database="DATA2DAY_DEMO",
        ),
        "sensor_io_manager": PandasParquetIOManager(root_path=SENSOR_DIRECTORY),
    },
)
