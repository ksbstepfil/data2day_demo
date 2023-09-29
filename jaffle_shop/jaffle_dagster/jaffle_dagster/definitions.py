import os

from dagster import Definitions, EnvVar, DagsterInvalidDefinitionError
from dagster_dbt import DbtCliResource
from dagster_snowflake_pandas import SnowflakePandasIOManager

from .assets import assets
from .constants import dbt_project_dir
from .schedules import schedules
from .sensors import my_directory_sensor
from .jobs import all_assets_job

defs = Definitions(
    assets=assets,
    schedules=schedules,
    sensors=[my_directory_sensor],
    jobs=[all_assets_job],
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
        "io_manager": SnowflakePandasIOManager(
            account="xskqzat-bk95941",
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            database="DATA2DAY_DEMO",  # required
            # role="writer",  # optional, defaults to the default role for the account
            # warehouse="PLANTS",  # optional, defaults to default warehouse for the account
            # schema="IRIS",  # optional, defaults to PUBLIC
        )
    },
)