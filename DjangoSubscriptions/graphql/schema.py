import graphene
from graphene_django_subscriptions.subscription import Subscription

from DjangoSubscriptions.serializers import UserSerializer


class UserSubscription(Subscription):
    class Meta:
        serializer_class = UserSerializer
        stream = 'users'
        description = 'User Subscription'


class Subscriptions(graphene.ObjectType):
    user_subscription = UserSubscription.Field()
