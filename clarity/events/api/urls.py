from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDeleteView,ApplyToEventListCreateView,ApplyToEventRetrieveUpdateDeleteView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='Event_list_create'),
    path('events/<int:pk>/', EventRetrieveUpdateDeleteView.as_view(), name='Event_retrieve_update_delete'),
        path('applyevents/', ApplyToEventListCreateView.as_view(), name='ApplyToEventListCreateView'),
    path('applyevents/<int:pk>/', ApplyToEventRetrieveUpdateDeleteView.as_view(), name='ApplyToEventRetrieveUpdateDeleteView'),
]
