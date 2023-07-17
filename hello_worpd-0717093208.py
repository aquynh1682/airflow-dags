from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_worpd-0717093208",
}

dag = DAG(
    "hello_worpd-0717093208",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_worpd.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_9b5ae55e_2efb_47ed_84e9_a30459ff8388 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_worpd-0717093208",
    cos_dependencies_archive="hello-9b5ae55e-2efb-47ed-84e9-a30459ff8388.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9b5ae55e_2efb_47ed_84e9_a30459ff8388.image_pull_policy = "IfNotPresent"


notebook_op_d4532ccc_9985_4282_88e7_3416a1466cc6 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_worpd-0717093208",
    cos_dependencies_archive="world-d4532ccc-9985-4282-88e7-3416a1466cc6.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
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

notebook_op_d4532ccc_9985_4282_88e7_3416a1466cc6.image_pull_policy = "IfNotPresent"

(
    notebook_op_d4532ccc_9985_4282_88e7_3416a1466cc6
    << notebook_op_9b5ae55e_2efb_47ed_84e9_a30459ff8388
)
