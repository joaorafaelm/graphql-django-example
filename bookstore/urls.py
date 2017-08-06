from django.conf.urls import url
from django.contrib import admin
from graphene_django.views import GraphQLView
from bookstore.schema import schema

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
