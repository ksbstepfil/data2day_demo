import pandas as pd
from dagster import OpExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets

from .constants import DBT_MANIFEST_PATH


@asset(compute_kind="python", io_manager_key="snowflake_io_manager")
def raw_customers(context) -> pd.DataFrame:
    data = pd.read_csv("https://docs.dagster.io/assets/customers.csv")

    context.add_output_metadata({"num_rows": data.shape[0]})
    return data


@asset(compute_kind="python", io_manager_key="snowflake_io_manager")
def raw_orders(context) -> pd.DataFrame:
    data = pd.read_csv(
        "../../raw_data/raw_orders.csv"
    )  # ("https://github.com/ksbstepfil/data2day_demo/commit/d137b09f4eaf8c8fa18ffaccf6ddac74f3bc7535#diff-f0b4b5aac87946e54b6ed620053077c8b7fa8769fa184bb7ce5ff5fd6195a08a") # ("../../raw_data/raw_orders.csv") # /Users/filipstepniak/PARA/1_Projects/data2day_demo/raw_data/raw_orders.csv") #

    context.add_output_metadata({"num_rows": data.shape[0]})
    return data


@asset(compute_kind="python", io_manager_key="snowflake_io_manager")
def raw_payments(context) -> pd.DataFrame:  # -> None:
    data = pd.read_csv("../../raw_data/raw_payments.csv")

    context.add_output_metadata({"num_rows": data.shape[0]})
    return data


@dbt_assets(manifest=DBT_MANIFEST_PATH, io_manager_key="snowflake_io_manager")
def jaffle_shop_dbt_assets(context: OpExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


assets = [raw_customers, raw_orders, raw_payments, jaffle_shop_dbt_assets]
