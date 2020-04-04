from django.urls import path, include
from .views import ListFilms, CreateFilms, UpdateFilms, DeleteFilms, DetailFilms
urlpatterns = [
    path('list/', ListFilms.as_view() ),
    path('create/', CreateFilms.as_view()),
    path('update/<int:pk>', UpdateFilms.as_view()),
    path('delete/<int:pk>', DeleteFilms.as_view()),
    path('detail/<int:pk>', DetailFilms.as_view())
]