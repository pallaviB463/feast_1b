from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32


# Entity
user = Entity(
    name="user_id",
    join_keys=["user_id"],
)


# Offline source
user_source = FileSource(
    name="user_features_source",
    path="data/user_features.parquet",
    timestamp_field="event_timestamp",
)


# Feature view
user_features_view = FeatureView(
    name="user_features",
    entities=[user],
    ttl=timedelta(days=1),
    schema=[
        Field(name="feature_1", dtype=Float32),
        Field(name="feature_2", dtype=Float32),
        Field(name="feature_3", dtype=Float32),
    ],
    source=user_source,
    online=True,
)