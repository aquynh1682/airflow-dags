from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0714070021",
}

dag = DAG(
    "hello_world-0714070021",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_1f8d224b_9542_479b_af01_5981745c63a1 = NotebookOp(
    name="Hello",
    namespace="ml-workshop",
    task_id="Hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/Hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0714070021",
    cos_dependencies_archive="Hello-1f8d224b-9542-479b-af01-5981745c63a1.tar.gz",
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

notebook_op_1f8d224b_9542_479b_af01_5981745c63a1.image_pull_policy = "IfNotPresent"


notebook_op_97aa5624_b480_4969_a47d_bc649ff0c457 = NotebookOp(
    name="World",
    namespace="ml-workshop",
    task_id="World",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/World.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-0714070021",
    cos_dependencies_archive="World-97aa5624-b480-4969-a47d-bc649ff0c457.tar.gz",
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

notebook_op_97aa5624_b480_4969_a47d_bc649ff0c457.image_pull_policy = "IfNotPresent"

(
    notebook_op_97aa5624_b480_4969_a47d_bc649ff0c457
    << notebook_op_1f8d224b_9542_479b_af01_5981745c63a1
)
