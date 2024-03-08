from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [
    #path('',views.index,name='index'),
    path('',views.MovieList.as_view(),name="index"),

    #path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('movie/<int:pk>',views.MovieDetail.as_view(),name="detail"),

    #path('add/',views.add_movie,name='add_movie'),
    path('add/',views.Movieadd.as_view(), name="add_movie"),

    #path('update/<int:id>/',views.update,name='update'),
    path('update/<int:pk>/',views.Movieupdate.as_view(), name="update"),

   # path('delete/<int:id>/', views.delete, name='delete'),
    path('delete/<int:pk>/',views.Moviedelete.as_view(), name="delete"),
]
