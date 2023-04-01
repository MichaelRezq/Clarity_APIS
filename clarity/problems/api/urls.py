from django.urls import path
from .views import get_post_problems,get_edit_delete_problem,get_post_solution,get_edit_delete_solution,LikeView\
    # ,LikeListCreateView,LikeRetrieveUpdateDeleteView

urlpatterns = [
    path('problems/', get_post_problems, name='problem_list_create'),
    path('problems/<int:pk>/', get_edit_delete_problem, name='problem_retrieve_update_delete'),
    path('solution/<int:problemID>/', get_post_solution, name='solutions'),
    path('solution/<int:problemID>/<int:solutionID>', get_edit_delete_solution, name='solutions_retrieve_update_delete'),
    path('solution/<int:post_id>/like', LikeView.as_view(), name='like_view'),
    # path('solution/<int:solution_id>/help', LikeRetrieveUpdateDeleteView.as_view(), name='like_view'),

]
