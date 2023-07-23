from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "HelloWorld-0723124407",
}

dag = DAG(
    "HelloWorld-0723124407",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using HelloWorld.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_f773b57f_28da_4780_8209_10c8af57cf64 = NotebookOp(
    name="Hello",
    namespace="ml-workshop",
    task_id="Hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/Hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="HelloWorld-0723124407",
    cos_dependencies_archive="Hello-f773b57f-28da-4780-8209-10c8af57cf64.tar.gz",
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

notebook_op_f773b57f_28da_4780_8209_10c8af57cf64.image_pull_policy = "IfNotPresent"


notebook_op_d1b5182b_5ae9_476f_a8cb_fac58ec32d65 = NotebookOp(
    name="World",
    namespace="ml-workshop",
    task_id="World",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/World.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="HelloWorld-0723124407",
    cos_dependencies_archive="World-d1b5182b-5ae9-476f-a8cb-fac58ec32d65.tar.gz",
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

notebook_op_d1b5182b_5ae9_476f_a8cb_fac58ec32d65.image_pull_policy = "IfNotPresent"

(
    notebook_op_d1b5182b_5ae9_476f_a8cb_fac58ec32d65
    << notebook_op_f773b57f_28da_4780_8209_10c8af57cf64
)
