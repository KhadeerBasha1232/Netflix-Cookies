from django.urls import path
from . import views
urlpatterns = [
    path('netflix/', views.get, name='Netflix'),
    path('randomize-content/', views.get_random_content, name='randomize_content'),
    path('',views.index,name="Index"),
    path('upload/', views.post , name='upload'),
    # Add other URLs as needed
]
