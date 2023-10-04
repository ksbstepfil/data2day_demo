import os
from dagster import sensor, RunRequest, RunConfig
from .jobs import FileConfig, log_file_job

MY_DIRECTORY = "/Users/filipstepniak/PARA/1_Projects/data2day_demo/parquet_samples/"

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
