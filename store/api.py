from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import SessionAuthentication
from tastypie import fields
from .models import Review, Book


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['username']
        authentication = SessionAuthentication()


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get']
        authentication = SessionAuthentication()


class ReviewResource(ModelResource):
    book = fields.ToOneField(BookResource, 'book')
    user = fields.ToOneField(UserResource, 'user', full=True)

    class Meta:
        queryset = Review.objects.all()
        allowed_methods = ['get']
        authentication = SessionAuthentication()
        filtering = {
            'book': ALL_WITH_RELATIONS
        }