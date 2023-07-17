from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "Module_deploy-0717102106",
}

dag = DAG(
    "Module_deploy-0717102106",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using Module_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_1a62dbb5_1c89_49a0_a8e5_6e88e85aca77 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="Module_deploy-0717102106",
    cos_dependencies_archive="build_push_image-1a62dbb5-1c89-49a0-a8e5-6e88e85aca77.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "https://quay.io",
        "CONTAINER_REGISTRY_USER": "quynhngo113",
        "CONTAINER_REGISTRY_PASSWORD": "Quynhlp123456a@",
        "CONTAINER_DETAILS": "quynhngo113/hellomlflow-manual:1.0.0",
    },
    config_file="None",
    dag=dag,
)

notebook_op_1a62dbb5_1c89_49a0_a8e5_6e88e85aca77.image_pull_policy = "IfNotPresent"


notebook_op_a8b19eae_b54a_4d5d_b215_36ffc91ded32 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="Module_deploy-0717102106",
    cos_dependencies_archive="deploy_model-a8b19eae-b54a-4d5d-b215-36ffc91ded32.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAIL": "quynhngo113/hellomlflow-manual:1.0.0",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a8b19eae_b54a_4d5d_b215_36ffc91ded32.image_pull_policy = "IfNotPresent"

(
    notebook_op_a8b19eae_b54a_4d5d_b215_36ffc91ded32
    << notebook_op_1a62dbb5_1c89_49a0_a8e5_6e88e85aca77
)
