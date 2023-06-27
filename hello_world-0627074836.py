from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0627074836",
}

dag = DAG(
    "hello_world-0627074836",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_6a5e54ea_440a_47f0_922a_28b1550a7526 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0627074836",
    cos_dependencies_archive="hello-6a5e54ea-440a-47f0-922a-28b1550a7526.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/repository/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_6a5e54ea_440a_47f0_922a_28b1550a7526.image_pull_policy = "IfNotPresent"


notebook_op_5ba230f0_0912_4fde_8907_473ee99771d1 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0627074836",
    cos_dependencies_archive="world-5ba230f0-0912-4fde-8907-473ee99771d1.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/repository/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5ba230f0_0912_4fde_8907_473ee99771d1.image_pull_policy = "IfNotPresent"

(
    notebook_op_5ba230f0_0912_4fde_8907_473ee99771d1
    << notebook_op_6a5e54ea_440a_47f0_922a_28b1550a7526
)
