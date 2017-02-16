from texts.models import Text
from calls.models import Call
from contacts.models import Contact
from api.serializers import TextSerializer, CallSerializer, ContactSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, permissions, views
from rest_framework.views import APIView

# from api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

from rest_framework_extensions.etag.mixins import ETAGMixin
from rest_framework_extensions.etag.decorators import etag


class TextViewSet(ETAGMixin, viewsets.ModelViewSet):

    serializer_class = TextSerializer

    def get_queryset(self):
        """Get queryset for photographer."""
        return Text.objects.all()

    def get_object(self):
        import pdb; pdb.set_trace
        return Text.objects.reverse()[0]


class CallViewSet(viewsets.ModelViewSet):

    serializer_class = CallSerializer

    def get_queryset(self):
        """Get queryset for photographer."""
        return Call.objects.all()


class ContactViewSet(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class LastText(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self):
        return Text.objects.order_by('id').reverse()[0]

    def get(self, request, format=None):
        snippet = self.get_object()
        serializer = TextSerializer(snippet)
        return Response(serializer.data)






# class TextViewSet(ETAGMixin, viewsets.ModelViewSet):

#     serializer_class = TextSerializer
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

#     @etag()
#     def list(self, request, *args, **kwargs):
#         return super(TextViewSet, self).list(request, *args, **kwargs)

#     @etag()
#     def retrieve(self, request, *args, **kwargs):
#         return super(TextViewSet, self).retrieve(request, *args, **kwargs)

#     def get_queryset(self):
#         """Get queryset for photographer."""
#         return Text.objects.all()
