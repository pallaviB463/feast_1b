from feast import FeatureStore
from datetime import datetime

store = FeatureStore(repo_path=".")

store.materialize_incremental(
    end_date=datetime.utcnow()
)