from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "build_push_image-0628030753",
}

dag = DAG(
    "build_push_image-0628030753",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using build_push_image.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_b83e38f1_1cfd_4eda_8a0a_1bfbaf3d1163 = NotebookOp(
    name="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    namespace="ml-workshop",
    task_id="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="build_push_image-0628030753",
    cos_dependencies_archive="build_push_image-b83e38f1-1cfd-4eda-8a0a-1bfbaf3d1163.tar.gz",
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

notebook_op_b83e38f1_1cfd_4eda_8a0a_1bfbaf3d1163.image_pull_policy = "Never"
