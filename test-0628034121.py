from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "test-0628034121",
}

dag = DAG(
    "test-0628034121",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using test.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_fcfcd3cf_0116_4aa3_9742_6a9581a8251b = NotebookOp(
    name="test_build",
    namespace="ml-workshop",
    task_id="test_build",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/test-build.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="test-0628034121",
    cos_dependencies_archive="test-build-fcfcd3cf-0116-4aa3-9742-6a9581a8251b.tar.gz",
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

notebook_op_fcfcd3cf_0116_4aa3_9742_6a9581a8251b.image_pull_policy = "Never"
