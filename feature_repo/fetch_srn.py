from feast import FeatureStore
import pandas as pd
from datetime import timezone

store = FeatureStore(repo_path=".")

SRN = "PES1UG24AM906"

FEATURES = [
    "user_features:feature_1",
    "user_features:feature_2",
    "user_features:feature_3",
]


# OFFLINE PATH
entity_df = pd.DataFrame.from_dict({
    "user_id": [SRN],
    "event_timestamp": [pd.Timestamp.now(timezone.utc)],
})

offline = store.get_historical_features(
    entity_df=entity_df,
    features=FEATURES,
).to_df()

print("OFFLINE (historical) features:")
print(offline)


# ONLINE PATH
online = store.get_online_features(
    features=FEATURES,
    entity_rows=[
        {"user_id": SRN}
    ],
).to_dict()

print("\nONLINE (materialized) features:")
print(online)