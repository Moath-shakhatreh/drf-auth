from django.urls import path

from .views import SnacklistView,SnackDetailView
urlpatterns = [
   
   path('',SnacklistView.as_view(), name= 'snack_list'),
   path('<int:pk>/',SnackDetailView.as_view(), name= 'snack_detail')

]