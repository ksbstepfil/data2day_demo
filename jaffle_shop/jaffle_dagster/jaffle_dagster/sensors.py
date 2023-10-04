import os
from dagster import sensor, RunRequest, RunConfig
from .constants import SENSOR_DIRECTORY
from .jobs import FileConfig, log_file_job


@sensor(job=log_file_job)
def my_directory_sensor():
    for filename in os.listdir(SENSOR_DIRECTORY):
        filepath = os.path.join(SENSOR_DIRECTORY, filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config=RunConfig(
                    ops={"process_file": FileConfig(filename=filename)}
                ),
            )
