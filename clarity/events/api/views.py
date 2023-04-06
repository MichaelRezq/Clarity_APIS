from rest_framework import generics, filters, permissions
from events.models import Event,ApplyToEvent
from .serializers import EventSerializer,ApplyToEventSerializer,EventPatchSerializer
from posts.api.views import CustomPagination
from permissions import IsAutherOrReadOnly
from rest_framework.response import Response
from rest_framework import generics, status
from django .conf import settings
from users.models import Custom
# ------------------- Events -------------------

# List all Events or create a new Event
class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['content','title']  # Specify the fields to search

    def get_queryset(self):
        user_community = self.request.user.community
        return Event.objects.filter(community=user_community)

# Retrieve, update or delete a Event instance
class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAutherOrReadOnly]

    def patch(self, request, *args, **kwargs):
        self.serializer_class = EventPatchSerializer
        event = self.get_object() # Get the Event object to modify
        user_id = request.data.get('user_id') # Get the user id to remove
        print('----------in Patch fun--event---------',event.applied_by.all())
        
        if user_id is not None:
            user = Custom.objects.get(id=user_id)

            # for deleting a user
            if user in event.applied_by.all() :
                try:
                    print("-----------the user is trying to un apply to an event----------------")

                    event.applied_by.remove(user) # Remove the user from the applied_by field
                    return Response(status=status.HTTP_200_OK)
                except :
                    return Response({'error': 'error during deleting the user'}, status=status.HTTP_400_BAD_REQUEST)
                    # for adding a user
            else:
                try:
                    print("-----------the user is trying to apply to an event----------------")
                    print("-----------user_id----------------",user_id)
                    user = Custom.objects.get(id=user_id)
                    print("-----------user----------------",user)
                    event.applied_by.add(user) # add the user from the applied_by field
                    return Response(status=status.HTTP_200_OK)
                except :
                    return Response({'error': 'error during adding the user'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error': 'User ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

        # partial = kwargs.pop('partial', False)
        # instance = self.get_object()
        # serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)


# ------------------- Apply to Events -------------------

# List all Events or create a new Event
class ApplyToEventListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplyToEventSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['event']  # Specify the fields to search

    # def get_queryset(self):
    #     user_community = self.request.user.community
    #     return Event.objects.filter(community=user_community)

# Retrieve, update or delete a Event instance
class ApplyToEventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplyToEvent.objects.all()
    serializer_class = ApplyToEventSerializer
