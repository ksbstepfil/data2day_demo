from dagster import ScheduleDefinition
from .jobs import all_but_sensor_job

all_but_sensor_schedule = ScheduleDefinition(job=all_but_sensor_job, cron_schedule="47 13 * * *", execution_timezone="Europe/Berlin")

schedules = [all_but_sensor_schedule]
