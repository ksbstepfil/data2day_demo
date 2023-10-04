import os
from dagster import sensor, RunRequest, RunConfig
from .constants import SENSOR_DIRECTORY
from .jobs import sensor_job


@sensor(job=sensor_job)
def my_directory_sensor():
    for filename in os.listdir(SENSOR_DIRECTORY):
        filepath = os.path.join(SENSOR_DIRECTORY, filename)
        if os.path.isfile(filepath) and filepath.endswith(".parquet"):
            yield RunRequest(run_key=filename)
