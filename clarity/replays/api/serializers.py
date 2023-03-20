from rest_framework import serializers
from replays.models import Reply

class CommentReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_id = serializers.IntegerField(source='comment.post.id')
    comment_id = serializers.IntegerField(source='comment.id')

    class Meta:
        model = Reply
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'post_id', 'comment_id', 'parent']

class CommentReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['content', 'parent']
