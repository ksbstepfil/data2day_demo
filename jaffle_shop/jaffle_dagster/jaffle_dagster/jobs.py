
from dagster import Config, ScheduleDefinition, define_asset_job, job, op

class FileConfig(Config):
    filename: str

@op
def process_file(context, config: FileConfig) -> None:
    context.log.info(config.filename)


@job
def log_file_job():
    process_file()

dbt_assets_job = define_asset_job(name="all_assets_job")
    #selection=["raw_customers", "raw_orders", "raw_payments", "jaffle_shop_dbt_assets"])
# all_assets_job = define_asset_job(name="all_assets_job")
