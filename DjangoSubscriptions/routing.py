from channels import include

from DjangoSubscriptions.graphql.routing import app_routing

channel_routing = [
    include("DjangoSubscriptions.graphql.routing.app_routing", path=r"^/subscriptions"),
]
