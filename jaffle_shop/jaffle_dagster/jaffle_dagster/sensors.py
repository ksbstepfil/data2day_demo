import os
from dagster import sensor, RunRequest, RunConfig
from .jobs import FileConfig, log_file_job

MY_DIRECTORY = "../../sensor_demo/"


@sensor(job=log_file_job)
def my_directory_sensor():
    for filename in os.listdir(MY_DIRECTORY):
        filepath = os.path.join(MY_DIRECTORY, filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config=RunConfig(
                    ops={"process_file": FileConfig(filename=filename)}
                ),
            )
