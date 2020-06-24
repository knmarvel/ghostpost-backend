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
    
    # queryset = GhostPost.objects.all().order_by(ordering_by)
    serializer_class = GhostPostSerializer

    def get_queryset(self):
        """
        This view filters and sorts the posts according to the URL
        """
        filter_sort_info = self.request.query_params
        print(filter_sort_info)
        queryset = ""
        if filter_sort_info["brn"] == "n":
            queryset = GhostPost.objects.all()
        elif filter_sort_info["brn"] == "b":
            queryset = GhostPost.objects.filter(boast=True)
            print(queryset)
        else:
            queryset = GhostPost.objects.filter(boast=False)
        if filter_sort_info['sort-by'] == "score":
            queryset = sorted(queryset, key = lambda a : -a.score())
        elif filter_sort_info['sort-by'] == "-score":
            queryset = sorted(queryset, key = lambda a : a.score())
        else:
            sort_by = self.request.query_params['sort-by']
            queryset = queryset.order_by(sort_by)
        return queryset

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
