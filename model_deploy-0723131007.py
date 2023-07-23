from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0723131007",
}

dag = DAG(
    "model_deploy-0723131007",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_70cded9c_d0cb_4d45_a0d8_3902301f7a0c = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0723131007",
    cos_dependencies_archive="build_push_image-70cded9c-d0cb-4d45-a0d8-3902301f7a0c.tar.gz",
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
        "CONTAINER_REGISTRY": "https://index.docker.io/v1/",
        "CONTAINER_REGISTRY_USER": "quynhngo113",
        "CONTAINER_REGISTRY_PASSWORD": "Quynhlp123456a@",
        "CONTAINER_DETAILS": "quynhngo113/mlflowdemo:v1.0.0",
    },
    config_file="None",
    dag=dag,
)

notebook_op_70cded9c_d0cb_4d45_a0d8_3902301f7a0c.image_pull_policy = "IfNotPresent"


notebook_op_5d9cdd04_a008_4a1f_b796_c225309691ab = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0723131007",
    cos_dependencies_archive="deploy_model-5d9cdd04-a008-4a1f-b796-c225309691ab.tar.gz",
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
        "CONTAINER_DETAILS": "quynhngo113/mlflowdemo:v1.0.0",
        "CLUSTER_DOMAIN_NAME": "vedlab.com",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5d9cdd04_a008_4a1f_b796_c225309691ab.image_pull_policy = "IfNotPresent"

(
    notebook_op_5d9cdd04_a008_4a1f_b796_c225309691ab
    << notebook_op_70cded9c_d0cb_4d45_a0d8_3902301f7a0c
)
