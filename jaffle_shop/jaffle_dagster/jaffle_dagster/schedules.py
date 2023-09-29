"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
# from dagster_dbt import build_schedule_from_dbt_selection

# from .assets import jaffle_shop_dbt_assets

from dagster import ScheduleDefinition
from .jobs import all_assets_job

basic_schedule = ScheduleDefinition(job=all_assets_job, cron_schedule="39 9 * * *")

schedules = [
    basic_schedule
#     build_schedule_from_dbt_selection(
#         [jaffle_shop_dbt_assets],
#         job_name="materialize_dbt_models",
#         cron_schedule="0 0 * * *",
#         dbt_select="fqn:*",
#     ),
]