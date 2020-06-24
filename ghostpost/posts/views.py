from ghostpost.posts.models import GhostPost
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ghostpost.posts.serializers import GhostPostSerializer
from ghostpost.posts.helpers import private_url_maker

# Create your views here.

class GhostPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ghostposts to be viewed or edited
    """
    queryset = GhostPost.objects.all().order_by('-datetime')
    serializer_class = GhostPostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=id):
        post = GhostPost.objects.get(pk=pk)
        post.upvotes += 1
        post.save()
        return Response({'status': 'Upvoted!'})
    
    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=id):
        post = GhostPost.objects.get(pk=pk)
        post.downvotes += 1
        post.save()
        return Response({'status': 'Downvoted!'})
