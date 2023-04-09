from django.urls import path

from .views import get_skill , get_update_skill
urlpatterns = [
      path('skills/', get_skill, name='skills'),
      path('skills/<int:id>/', get_update_skill , name='skill'),

]
