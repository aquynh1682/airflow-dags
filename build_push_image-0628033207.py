from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "build_push_image-0628033207",
}

dag = DAG(
    "build_push_image-0628033207",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using build_push_image.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_1985586b_b4c7_4721_ab13_13ac74f75812 = NotebookOp(
    name="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    namespace="ml-workshop",
    task_id="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="build_push_image-0628033207",
    cos_dependencies_archive="build_push_image-1985586b-b4c7-4721-ab13-13ac74f75812.tar.gz",
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

notebook_op_1985586b_b4c7_4721_ab13_13ac74f75812.image_pull_policy = "Never"
