import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene_django_subscriptions.subscription import Subscription

from DjangoSubscriptions.serializers import UserSerializer


class UserInterface(graphene.Interface):
    username = graphene.String()


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


'''
class UserSubscription(Subscription):
    class Meta:
        serializer_class = UserSerializer
        stream = 'users'
        description = 'User Subscription'
        interfaces = (graphene.Node,)


class Subscriptions(graphene.ObjectType):
    user_subscription = UserSubscription.Field()
'''
