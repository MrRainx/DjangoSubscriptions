from channels.routing import route_class
from graphql_ws.django_channels import GraphQLSubscriptionConsumer

channel_routing = [
    route_class(GraphQLSubscriptionConsumer, path=r"^/subscriptions"),
]
