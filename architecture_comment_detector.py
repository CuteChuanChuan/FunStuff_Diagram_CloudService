from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import ComputeEngine, Run, Functions
from diagrams.gcp.devtools import ContainerRegistry
from diagrams.gcp.network import LoadBalancing, NAT
from diagrams.gcp.operations import Monitoring
from diagrams.onprem.container import Docker
from diagrams.onprem.database import MongoDB
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.inmemory import Redis
from diagrams.programming.framework import Fastapi
from diagrams.programming.language import Python


with Diagram(name="Comment Detector Architecture", show=False):
    crawler = ComputeEngine("Crawler")
    api = Run("API")
    db = MongoDB("Primary Database")
    rd = Redis("Cached Database")
    crawler >> db
    db >> rd
    rd >> api
    db >> api
