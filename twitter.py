from diagrams import Cluster, Diagram
from diagrams.programming.language import Python
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import RabbitMQ
from diagrams.saas.chat import Slack
from diagrams.generic.network import Router
from diagrams.generic.os import Windows
from diagrams.elastic.elasticsearch import Elasticsearch

with Diagram("Twitter-like App Architecture", show=False):
  with Cluster("Client Side"):
    client = Python("Client")

  with Cluster("Server Side"):
    server = Python("Server")
    auth = Python("Auth & Authorization")

  with Cluster("Data Store"):
    database = PostgreSQL("Database")
    cache = Redis("Cache")

  with Cluster("Messaging Queue"):
    mq = RabbitMQ("Message Queue")

  with Cluster("Search Engine"):
    search = Elasticsearch("Search")

  with Cluster("Deployment & Monitoring"):
    deploy_monitoring = Slack("Deployment & Monitoring")

  client >> server >> [database, cache, mq, search, auth, deploy_monitoring]
