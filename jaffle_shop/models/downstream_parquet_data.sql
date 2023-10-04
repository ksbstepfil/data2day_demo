select *
from {{ source('PUBLIC', 'source_parquet_data') }}
