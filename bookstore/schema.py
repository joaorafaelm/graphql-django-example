import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.debug import DjangoDebug
from bookstore.store.models import Author, Book, Publisher


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class BookType(DjangoObjectType):
    authors = graphene.List(AuthorType)

    # Many To Many fix until next release.
    # https://github.com/graphql-python/graphene-django/issues/155
    @graphene.resolve_only_args
    def resolve_authors(self):
        return self.authors.all()

    class Meta:
        model = Book


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_books = graphene.List(BookType)
    all_publishers = graphene.List(PublisherType)

    # Debug field (rawSql, parameters etc).
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_authors(self, args, context, info):
        return Author.objects.all()

    def resolve_all_books(self, args, context, info):
        return Book.objects.select_related('publisher').all()

    def resolve_all_publishers(self, args, context, info):
        return Publisher.objects.all()

schema = graphene.Schema(query=Query)
