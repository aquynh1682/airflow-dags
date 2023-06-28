from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0628024253",
}

dag = DAG(
    "model_deploy-0628024253",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_30e0375e_66aa_4f9a_994c_77e7814be449 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0628024253",
    cos_dependencies_archive="build_push_image-30e0375e-66aa-4f9a-994c-77e7814be449.tar.gz",
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
        "CONTAINER_REGISTRY": "https://quay.io/",
        "CONTAINER_REGISTRY_USER": "lighty55",
        "CONTAINER_REGISTRY_PASSWORD": "spoody51299",
        "CONTAINER_DETAILS": "lighty55/mlflowdemo:1.11",
    },
    config_file="None",
    dag=dag,
)

notebook_op_30e0375e_66aa_4f9a_994c_77e7814be449.image_pull_policy = "Never"


notebook_op_c0f66c8c_ea82_4b96_8fac_5ba1451f39c2 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deploy-0628024253",
    cos_dependencies_archive="deploy_model-c0f66c8c-ea82-4b96-8fac-5ba1451f39c2.tar.gz",
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
        "CONTAINER_REGISTRY_USER": "lighty55",
        "CONTAINER_REGISTRY": "https://quay.io/",
    },
    config_file="None",
    dag=dag,
)

notebook_op_c0f66c8c_ea82_4b96_8fac_5ba1451f39c2.image_pull_policy = "Never"

(
    notebook_op_c0f66c8c_ea82_4b96_8fac_5ba1451f39c2
    << notebook_op_30e0375e_66aa_4f9a_994c_77e7814be449
)
