#!/usr/bin/env python3
import os

#from aws_cdk import core as cdk
from aws_cdk import core
from docker_pipeline.docker_pipeline import DockerPipelineConstruct
from terraform_pipeline.terraform_pipeline_stack import TerraformPipelineStack

app = core.App()
name = app.node.try_get_context("name")
container_stack = core.Stack(scope=app,id=f"{name}-container-stack")

terraform_backend_stack = core.Stack(scope=app,id=f"{name}-backend-stack")
terraform_network_stack = core.Stack(scope=app,id=f"{name}-network-stack")
terraform_eks_stack     = core.Stack(scope=app,id=f"{name}-eks-stack")

#terraform_argocd_stack               = core.Stack(scope=app,id=f"{name}-argocd-stack")
terraform_aws_ebs_csi_driver_stack   = core.Stack(scope=app,id=f"{name}-aws-ebs-csi-driver-stack")
terraform_ingress_nginx_stack        = core.Stack(scope=app,id=f"{name}-ingress-nginx-stack")
terraform_cluster_autoscaler_stack   = core.Stack(scope=app,id=f"{name}-cluster-autoscaler-stack")
#terraform_newrelic_stack             = core.Stack(scope=app,id=f"{name}-newrelic-stack")
terraform_metrics_server_stack             = core.Stack(scope=app,id=f"{name}-metrics-server-stack")

terraform_cloudwatch_agent_for_log_stack                = core.Stack(scope=app,id=f"{name}-cloudwatch-agent-for-log-stack")
terraform_cloudwatch_agent_for_metrics_stack            = core.Stack(scope=app,id=f"{name}-cloudwatch-agent-for-metrics-stack")



docker_stack=DockerPipelineConstruct(
    scope=container_stack,
    id=f"{name}-docker-pipeline"
)  

tf_backend_stack=TerraformPipelineStack(
    scope=terraform_backend_stack, 
    id=f"{name}-backend",
    ecr_repository=docker_stack.container_repository
)

tf_network_stack=TerraformPipelineStack(
    scope=terraform_network_stack, 
    id=f"{name}-network",
    ecr_repository=docker_stack.container_repository
)

tf_eks_stack=TerraformPipelineStack(
    scope=terraform_eks_stack, 
    id=f"{name}-eks",
    ecr_repository=docker_stack.container_repository
)

# tf_argocd_stack=TerraformPipelineStack(
#     scope=terraform_argocd_stack, 
#     id=f"{name}-argo-cd",
#     ecr_repository=docker_stack.container_repository
# )

tf_aws_ebs_csi_driver_stack=TerraformPipelineStack(
    scope=terraform_aws_ebs_csi_driver_stack, 
    id=f"{name}-aws-ebs-csi-driver",
    ecr_repository=docker_stack.container_repository
)

tf_ingress_nginx_stack=TerraformPipelineStack(
    scope=terraform_ingress_nginx_stack, 
    id=f"{name}-ingress-nginx",
    ecr_repository=docker_stack.container_repository
)

tf_cluster_autoscaler_stack=TerraformPipelineStack(
    scope=terraform_cluster_autoscaler_stack, 
    id=f"{name}-cluster-autoscaler",
    ecr_repository=docker_stack.container_repository
)

tf_metrics_server_stack=TerraformPipelineStack(
    scope=terraform_metrics_server_stack, 
    id=f"{name}-metrics-server",
    ecr_repository=docker_stack.container_repository
)

tf_cloudwatch_agent_for_log_stack=TerraformPipelineStack(
    scope=terraform_cloudwatch_agent_for_log_stack,
    id=f"{name}-cloudwatch-agent-for-log",
    ecr_repository=docker_stack.container_repository
)

tf_cloudwatch_agent_for_metrics_stack=TerraformPipelineStack(
    scope=terraform_cloudwatch_agent_for_metrics_stack,
    id=f"{name}-cloudwatch-agent-for-metrics",
    ecr_repository=docker_stack.container_repository
)
app.synth()
