
from dagster import Config, ScheduleDefinition, define_asset_job, job, op

from .assets import sensor_parquet_data

# class FileConfig(Config):
#     filepath: str

# @op
# def process_file(context, config: FileConfig):
#     context.log.info(config.filepath)
#     define_asset_job(
#         name="job_sensor", selection=[sensor_parquet_data(filepath=config.filename)])

# @job
# def asset_job_sensor():
#     process_file()

dbt_assets_job = define_asset_job(name="all_assets_job")

asset_job_sensor = define_asset_job(
    name="job_sensor", selection=[sensor_parquet_data])

    #selection=["raw_customers", "raw_orders", "raw_payments", "jaffle_shop_dbt_assets"])
# all_assets_job = define_asset_job(name="all_assets_job")
