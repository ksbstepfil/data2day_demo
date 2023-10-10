import pandas as pd

from dagster import (
    OutputContext,
    InputContext,
    ConfigurableIOManager,
)


# adapted from example at https://docs.dagster.io/concepts/io-management/io-managers
class PandasParquetIOManager(ConfigurableIOManager):
    root_path: str

    def _get_path(self):
        return self.root_path

    def handle_output(self, context: OutputContext, obj):
        raise NotImplemented("This IO manager is read-only!")

    def load_input(self, context: InputContext):
        return pd.read_parquet(self._get_path())
