from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, Elasticache
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.network import Route53

with Diagram(name="Clustered Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [
            EC2("Web1"),
            EC2("Web2"),
            EC2("Web3"),
        ]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = Elasticache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
