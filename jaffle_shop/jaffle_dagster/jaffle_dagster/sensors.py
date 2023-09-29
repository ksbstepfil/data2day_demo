import os
from dagster import define_asset_job, sensor, RunRequest, RunConfig
from .assets import sensor_parquet_data
from .jobs import FileConfig, log_file_job

MY_DIRECTORY = "../../parquet_samples/"

asset_job_sensor = define_asset_job(name="job_sensor", selection=[sensor_parquet_data])

@sensor(job=asset_job_sensor)
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
