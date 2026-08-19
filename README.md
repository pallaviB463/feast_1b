# Feast 1B - Feature Store Implementation

## Student Details

- **SRN:** PES1UG24AM906
- **Course:** MLOps
- **Experiment:** Feast 1B
- **Framework:** Feast
- **Feast Version:** 0.65.0
- **Python Version:** 3.11.9

---

## 1. Objective

This project implements a feature store workflow using **Feast**.

The implementation demonstrates:

- Creating a Feast feature repository
- Defining an entity using `user_id`
- Creating a Feature View named `user_features`
- Using a Parquet file as the offline data source
- Defining and adding `feature_3`
- Applying the feature definitions using `feast apply`
- Materializing features into a SQLite online store
- Performing historical/offline feature retrieval
- Performing online feature retrieval
- Retrieving features using the student SRN

---

## 2. Project Structure

```text
feast_student_repo/
│
└── feature_repo/
    │
    ├── data/
    │   └── user_features.parquet
    │
    ├── feature_definitions.py
    ├── feature_store.yaml
    ├── sample_data.py
    ├── materialize.py
    ├── fetch_srn.py
    ├── test_workflow.py
    └── __init__.py
```

### File Description

| File | Purpose |
|---|---|
| `feature_definitions.py` | Defines the Feast project, entity, Feature View, and features |
| `feature_store.yaml` | Feast repository configuration |
| `sample_data.py` | Generates the sample Parquet data |
| `materialize.py` | Materializes features into the online store |
| `fetch_srn.py` | Retrieves features for the specified SRN |
| `test_workflow.py` | Tests the feature store workflow |
| `user_features.parquet` | Offline feature data source |

---

## 3. Environment Setup

### Python Version

The project uses:

```text
Python 3.11.9
```

Check the Python version:

```cmd
python --version
```

### Create Virtual Environment

```cmd
python -m venv feast-env
```

### Activate Virtual Environment

On Windows:

```cmd
feast-env\Scripts\activate
```

The terminal should show:

```text
(feast-env)
```

### Verify Python Environment

```cmd
where python
```

The first path should point to:

```text
feast-env\Scripts\python.exe
```

Verify the Python executable:

```cmd
python -c "import sys; print(sys.executable)"
```

---

## 4. Install Feast

Install Feast:

```cmd
pip install feast==0.65.0
```

Verify the installation:

```cmd
feast version
```

Expected:

```text
Feast SDK Version: "0.65.0"
```

---

## 5. Feature Repository

All Feast commands are executed from the `feature_repo` directory.

Example:

```cmd
cd feast_student_repo\feature_repo
```

The directory contains:

```text
feature_definitions.py
feature_store.yaml
sample_data.py
materialize.py
fetch_srn.py
test_workflow.py
data\
```

---

## 6. Feature Definition

The Feast project uses `user_id` as the entity.

### Entity

```python
user = Entity(
    name="user",
    join_keys=["user_id"]
)
```

### Feature View

The Feature View is:

```text
user_features
```

It contains the following features:

| Feature | Type |
|---|---|
| `feature_1` | Float32 |
| `feature_2` | Float32 |
| `feature_3` | Float32 |

The timestamp column is:

```text
event_timestamp
```

The source data is stored in:

```text
data/user_features.parquet
```

---

## 7. Sample Data

The sample data contains:

```text
user_id
event_timestamp
feature_1
feature_2
feature_3
```

Example:

| user_id | feature_1 | feature_2 | feature_3 |
|---|---:|---:|---:|
| PES1UG24AM906 | 0.42 | 1.1 | 5.5 |
| S2 | 0.77 | 2.4 | 6.6 |
| S3 | 0.15 | 0.9 | 7.7 |

The student's SRN is used as the `user_id` for the student-specific retrieval.

---

## 8. Generate Sample Data

Run:

```cmd
python sample_data.py
```

This generates:

```text
data/user_features.parquet
```

The generated Parquet file is used as the offline data source for Feast.

---

## 9. Apply Feast Definitions

Run:

```cmd
feast apply
```

This registers the project and Feature View with Feast.

The expected output includes:

```text
Applying changes for project feast_student_repo
Updated feature view user_features
```

The Feature View contains:

```text
feature_1
feature_2
feature_3
```

---

## 10. Feast Registry

The Feast Registry stores the metadata and definitions of the Feast objects.

The architecture is:

```text
feature_definitions.py
        |
        | feast apply
        v
+----------------------+
|    Feast Registry    |
|                      |
| Project              |
| Entity               |
| Feature View         |
| Feature Definitions  |
+----------------------+
```

The Registry contains the definitions required by Feast to manage and retrieve the features.

---

## 11. Offline Data Source

The offline source is:

```text
data/user_features.parquet
```

The Parquet file contains:

```text
user_id
event_timestamp
feature_1
feature_2
feature_3
```

This source is used for historical feature retrieval and for materialization into the online store.

---

## 12. Materialization

The features are materialized into a **SQLite online store**.

Run:

```cmd
python materialize.py
```

The materialization process loads feature values from the offline source into the online store.

The workflow is:

```text
user_features.parquet
        |
        | materialize
        v
+----------------------+
| SQLite Online Store  |
+----------------------+
```

The online store contains the latest available feature values required for online retrieval.

---

## 13. Historical / Offline Feature Retrieval

Historical features are retrieved using:

```text
get_historical_features()
```

The historical retrieval path is:

```text
user_features.parquet
        |
        v
get_historical_features()
        |
        v
Historical Feature Dataset
```

This path is used to retrieve feature values from historical timestamps and can be used to create datasets for model training.

---

## 14. Online Feature Retrieval

Online features are retrieved using:

```text
get_online_features()
```

The online retrieval path is:

```text
SQLite Online Store
        |
        v
get_online_features()
        |
        v
Student SRN
        |
        v
feature_1
feature_2
feature_3
```

For this implementation, the student-specific entity is:

```text
PES1UG24AM906
```

The retrieved values are:

```text
feature_1 = 0.42
feature_2 = 1.1
feature_3 = 5.5
```

---

## 15. Complete Architecture

The complete Feast architecture implemented in this project is:

```text
                       +--------------------------+
                       |  feature_definitions.py |
                       |                          |
                       | Entity: user_id          |
                       | Feature View:            |
                       | user_features            |
                       |                          |
                       | feature_1                |
                       | feature_2                |
                       | feature_3                |
                       +------------+-------------+
                                    |
                                    | feast apply
                                    v
                       +--------------------------+
                       |      Feast Registry      |
                       |                          |
                       | Project:                 |
                       | feast_student_repo       |
                       +--------------------------+


+----------------------------+
| user_features.parquet      |
|                            |
| user_id                    |
| event_timestamp            |
| feature_1                  |
| feature_2                  |
| feature_3                  |
+-------------+--------------+
              |
              |
       +------+---------------------------+
       |                                  |
       |                                  |
       v                                  v
+----------------------------+   +----------------------------+
| Historical Retrieval       |   | Materialization            |
|                            |   |                            |
| get_historical_features()  |   | materialize.py             |
+-------------+--------------+   +-------------+--------------+
              |                                |
              v                                |
+----------------------------+                 |
| Historical / Training      |                 |
| Dataset                    |                 |
+----------------------------+                 |
                                               |
                                               v
                                  +----------------------------+
                                  | SQLite Online Store       |
                                  +-------------+--------------+
                                                |
                                                |
                                                | get_online_features()
                                                v
                                  +----------------------------+
                                  | Online Feature Retrieval   |
                                  |                            |
                                  | SRN: PES1UG24AM906         |
                                  +-------------+--------------+
                                                |
                                                v
                                  +----------------------------+
                                  | Retrieved Features         |
                                  |                            |
                                  | feature_1 = 0.42           |
                                  | feature_2 = 1.1            |
                                  | feature_3 = 5.5            |
                                  +----------------------------+
```

---

## 16. Workflow Summary

The complete workflow can be summarized as:

```text
1. Create virtual environment
          |
          v
2. Install Feast
          |
          v
3. Generate sample data
   python sample_data.py
          |
          v
4. user_features.parquet
          |
          +------------------------+
          |                        |
          v                        v
5. Historical Retrieval      5. Materialization
   get_historical_features()       |
          |                        v
          |                  SQLite Online Store
          |                        |
          |                        v
          |                get_online_features()
          |                        |
          |                        v
          |                  Student SRN
          |                        |
          |                        v
          |                  feature_1
          |                  feature_2
          |                  feature_3
          |
          v
   Historical Dataset
```

---

## 17. Commands Used

The main commands used in the experiment are:

### Activate environment

```cmd
feast-env\Scripts\activate
```

### Check Python

```cmd
python --version
```

### Check Feast

```cmd
feast version
```

### Generate data

```cmd
python sample_data.py
```

### Apply Feast definitions

```cmd
feast apply
```

### Materialize features

```cmd
python materialize.py
```

### Fetch student features

```cmd
python fetch_srn.py
```

### Run workflow tests

```cmd
python test_workflow.py
```

---

## 18. Verification

The implementation was verified using:

- Successful execution of `feast apply`
- Successful creation of `user_features.parquet`
- Successful materialization into the SQLite online store
- Historical/offline feature retrieval
- Online feature retrieval
- Retrieval of three features for the student SRN

The final feature set contains:

```text
feature_1
feature_2
feature_3
```

---

## 19. Final Output

The student-specific online retrieval returns:

```text
SRN: PES1UG24AM906

feature_1 = 0.42
feature_2 = 1.1
feature_3 = 5.5
```

The implementation demonstrates that the same Feast Feature View can be used for both historical/offline retrieval and online feature serving.

---

## 20. Deliverables

The submission contains:

1. **Feature Repository**
   - Feast configuration
   - Feature definitions
   - Sample data generation
   - Materialization script
   - Feature retrieval script
   - Parquet data source

2. **Screenshots**
   - Feast environment/setup
   - `feast apply`
   - Materialization
   - Historical/offline retrieval
   - Online retrieval

3. **Architecture Diagram**
   - Offline data source
   - Feast Registry
   - SQLite Online Store
   - Historical retrieval path
   - Online retrieval path
   - Student SRN
   - Three features

---

## 21. Technologies Used

- Python 3.11.9
- Feast 0.65.0
- Pandas
- PyArrow
- Parquet
- SQLite
- Windows
- Git / GitHub

---

## 22. Repository

This repository contains the complete Feast 1B implementation and supporting files required to reproduce the feature store workflow.
