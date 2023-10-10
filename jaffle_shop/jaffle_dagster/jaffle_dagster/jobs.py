from dagster import define_asset_job, AssetSelection


all_but_sensor_job = define_asset_job(
    name="materialize_schedule",
    selection=AssetSelection.all() - AssetSelection.groups("sensor_demo"),
)

sensor_job = define_asset_job(
    name="materialize_sensor", selection=AssetSelection.groups("sensor_demo")
)
