from rest_framework import generics, permissions, status
from rest_framework.response import Response
from replays.models import Reply
from .serializers import CommentReplySerializer, CommentReplyCreateSerializer

class CommentReplyList(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CommentReplyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, comment_id=kwargs['comment_id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter by comment id if specified in query parameters
        comment_id = self.request.query_params.get('comment_id', None)
        if comment_id is not None:
            queryset = queryset.filter(comment_id=comment_id)
        return queryset

class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [permissions.AllowAny]
