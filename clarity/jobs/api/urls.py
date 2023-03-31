from django.urls import path
from . import views


urlpatterns = [
    path('jobs/',views.job_list, name='list_jobs'),
    path('jobs/<int:id>',views.job_one, name='one_job'),

]
