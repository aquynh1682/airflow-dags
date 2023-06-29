from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "flight-0629102851",
}

dag = DAG(
    "flight-0629102851",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using flight.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_03cc445a_7314_4d34_91d5_65033d06fd90 = NotebookOp(
    name="start_spark_cluster",
    namespace="ml-workshop",
    task_id="start_spark_cluster",
    notebook="Machine-Learning-on-Kubernetes/Chapter09/pipeline-helpers/start-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="flight-0629102851",
    cos_dependencies_archive="start-spark-cluster-03cc445a-7314-4d34-91d5-65033d06fd90.tar.gz",
    pipeline_outputs=["spark-info."],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "SPANK_CLUTSER": "ml-user-airflow-cluster",
        "WORKER_NODES": "2",
    },
    config_file="None",
    dag=dag,
)

notebook_op_03cc445a_7314_4d34_91d5_65033d06fd90.image_pull_policy = "IfNotPresent"


notebook_op_791f81fc_898b_4163_bede_da0d2162e9fa = NotebookOp(
    name="merge_data",
    namespace="ml-workshop",
    task_id="merge_data",
    notebook="Machine-Learning-on-Kubernetes/Chapter09/merge_data.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="flight-0629102851",
    cos_dependencies_archive="merge_data-791f81fc-898b-4163-bede-da0d2162e9fa.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info."],
    image="quay.io/ml-on-k8s/elyra-spark:0.0.4",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_791f81fc_898b_4163_bede_da0d2162e9fa.image_pull_policy = "IfNotPresent"

(
    notebook_op_791f81fc_898b_4163_bede_da0d2162e9fa
    << notebook_op_03cc445a_7314_4d34_91d5_65033d06fd90
)


notebook_op_d9b86a5a_dc23_461c_b175_d6515a60368b = NotebookOp(
    name="clean_data",
    namespace="ml-workshop",
    task_id="clean_data",
    notebook="Machine-Learning-on-Kubernetes/Chapter09/clean_data.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="flight-0629102851",
    cos_dependencies_archive="clean_data-d9b86a5a-dc23-461c-b175-d6515a60368b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info."],
    image="quay.io/ml-on-k8s/elyra-spark:0.0.4",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d9b86a5a_dc23_461c_b175_d6515a60368b.image_pull_policy = "IfNotPresent"

(
    notebook_op_d9b86a5a_dc23_461c_b175_d6515a60368b
    << notebook_op_791f81fc_898b_4163_bede_da0d2162e9fa
)


notebook_op_424ce7ae_69d5_48a1_a1e0_a67fc4630025 = NotebookOp(
    name="stop_spark_cluster",
    namespace="ml-workshop",
    task_id="stop_spark_cluster",
    notebook="Machine-Learning-on-Kubernetes/Chapter09/pipeline-helpers/stop-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="flight-0629102851",
    cos_dependencies_archive="stop-spark-cluster-424ce7ae-69d5-48a1-a1e0-a67fc4630025.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info."],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_424ce7ae_69d5_48a1_a1e0_a67fc4630025.image_pull_policy = "IfNotPresent"

(
    notebook_op_424ce7ae_69d5_48a1_a1e0_a67fc4630025
    << notebook_op_d9b86a5a_dc23_461c_b175_d6515a60368b
)
