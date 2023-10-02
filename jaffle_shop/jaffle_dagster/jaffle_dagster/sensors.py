import os
from dagster import define_asset_job, sensor, RunRequest, RunConfig
from .assets import MyAssetConfig
from .jobs import FileConfig, asset_job_sensor

MY_DIRECTORY = "../../sensor_dagster_test/"

@sensor(job=asset_job_sensor)
def my_directory_sensor():
    for filename in os.listdir(MY_DIRECTORY):
        filepath = os.path.join(MY_DIRECTORY, filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config=RunConfig(
                    {"sensor_parquet_data": MyAssetConfig(filepath=filepath)}
                # run_config=RunConfig(
                #     ops={"process_file": FileConfig(filepath=filepath)}
                ),
            )
