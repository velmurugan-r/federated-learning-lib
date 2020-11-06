import os

import wrapt

from kubernetes.client.configuration import Configuration
from kubernetes.config.incluster_config import load_incluster_config
from kubernetes.client.api_client import ApiClient
from kubernetes.client.rest import ApiException
from openshift.dynamic import DynamicClient

if os.environ.get('JUPYTERHUB_NOTEBOOK_CPU'):
    c.Spawner.cpu_limit = os.environ['JUPYTERHUB_NOTEBOOK_CPU']
