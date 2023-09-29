import os

import duckdb
import pandas as pd
import plotly.express as px
from dagster import MetadataValue, OpExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets, get_asset_key_for_model

from .constants import dbt_manifest_path, dbt_project_dir

@asset(compute_kind="python")
def raw_customers(context) -> pd.DataFrame: # -> None:
    data = pd.read_csv("https://docs.dagster.io/assets/customers.csv")

    context.add_output_metadata({"num_rows": data.shape[0]})
    return data

# @asset(compute_kind="python")
# def raw_orders(context) -> pd.DataFrame: # -> None:
#     data = pd.read_csv(
#         "../../raw_data/raw_orders.csv")

#     context.add_output_metadata({"num_rows": data.shape[0]})
#     return data

# @asset(compute_kind="python")
# def raw_payments(context) -> pd.DataFrame: # -> None:
#     data = pd.read_csv(
#         "../../raw_data/raw_payments.csv")

#     context.add_output_metadata({"num_rows": data.shape[0]})
#     return data

@dbt_assets(manifest=dbt_manifest_path)
def jaffle_shop_dbt_assets(context: OpExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

assets = [raw_customers, jaffle_shop_dbt_assets]
