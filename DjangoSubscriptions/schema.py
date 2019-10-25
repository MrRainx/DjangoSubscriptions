import graphene
from django.contrib.auth import get_user_model
from graphene import relay
from rx import Observable

import graphene

# from DjangoSubscriptions.graphql.schema import Subscriptions
from DjangoSubscriptions.graphql.schema import UserType


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return 'world'


'''
class Subscription(graphene.ObjectType):
    count_seconds = graphene.Int(up_to=graphene.Int(required=True))
    user_subscription = UserSubscription.Field()

    def resolve_count_seconds(root, info, up_to=5):
        return 1
        return Observable.interval(1000) \
            .map(lambda i: "{0}".format(i)) \
            .take_while(lambda i: int(i) <= up_to)
'''


class RootSubscription(graphene.ObjectType):
    test = graphene.Field(UserType)

    def resolve_user(self, info):
        return get_user_model().objects.all()

    class Meta:
        description = 'The project root subscription definition'


schema = graphene.Schema(
    query=Query,
    subscription=RootSubscription
)
