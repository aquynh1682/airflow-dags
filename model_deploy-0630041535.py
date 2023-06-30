from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0630041535",
}

dag = DAG(
    "model_deploy-0630041535",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_9656b70b_b273_4c0b_9cea_8fa84bfd5909 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0630041535",
    cos_dependencies_archive="build_push_image-9656b70b-b273-4c0b-9cea-8fa84bfd5909.tar.gz",
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
        "CONTAINER_REGISTRY": "https://quay.io/api/v1",
        "CONTAINER_REGISTRY_USER": "quynhngo113",
        "CONTAINER_REGISTRY_PASSWORD": "Quynhlp123456a@",
        "CONTAINER_DETAILS": "quynhngo113/mlflowdemo:latest",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9656b70b_b273_4c0b_9cea_8fa84bfd5909.image_pull_policy = "Never"


notebook_op_31574f1c_4274_40f5_8a4a_bcabd311f6e9 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0630041535",
    cos_dependencies_archive="deploy_model-31574f1c-4274-40f5-8a4a-bcabd311f6e9.tar.gz",
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
        "CONTAINER_REGISTRY": "https://quay.io/api/v1/",
    },
    config_file="None",
    dag=dag,
)

notebook_op_31574f1c_4274_40f5_8a4a_bcabd311f6e9.image_pull_policy = "IfNotPresent"

(
    notebook_op_31574f1c_4274_40f5_8a4a_bcabd311f6e9
    << notebook_op_9656b70b_b273_4c0b_9cea_8fa84bfd5909
)
