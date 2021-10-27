from django.urls import path,include

from . import views
urlpatterns = [

    path('list/',views.Showlist.as_view()),
    path('add/',views.Createlist.as_view()),
    path('delete/<int:pk>',views.Deleterec.as_view()),
    #path('api-auth/', include('rest_framework.urls'))
]