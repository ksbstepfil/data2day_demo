from dagster import define_asset_job, AssetSelection


all_assets_job = define_asset_job(name="all_assets_job")

sensor_job = define_asset_job(
    name="materialize_sensor", selection=AssetSelection.groups("sensor_demo")
)
