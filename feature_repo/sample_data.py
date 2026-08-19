import pandas as pd
from datetime import datetime, timedelta, timezone

df = pd.DataFrame({
    "user_id": ["PES1UG24AM906", "S2", "S3"],
    "event_timestamp": [
        datetime.now(timezone.utc) - timedelta(hours=i)
        for i in range(3)
    ],
    "feature_1": [0.42, 0.77, 0.15],
    "feature_2": [1.1, 2.4, 0.9],
    "feature_3": [5.5, 6.6, 7.7],
})

df.to_parquet("data/user_features.parquet")

print(df)
print("\nCreated data/user_features.parquet")