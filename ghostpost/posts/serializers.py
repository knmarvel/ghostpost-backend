from ghostpost.posts.models import GhostPost
from rest_framework import serializers


class GhostPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        fields = [
            'pk',
            'boast',
            'text',
            'upvotes',
            'downvotes',
            'private_url',
            'datetime'
        ]


