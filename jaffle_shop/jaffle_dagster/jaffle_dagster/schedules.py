from dagster import ScheduleDefinition
from .jobs import all_assets_job

basic_schedule = ScheduleDefinition(job=all_assets_job, cron_schedule="39 9 * * *")

schedules = [basic_schedule]
