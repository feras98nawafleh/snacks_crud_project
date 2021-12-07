from django.urls import path
from .views import  ( 
                        ListSnackView,
                        CreateSnackView,
                        DeleteSnackView,
                        UpdateSnackView,
                        DetailSnackView
                    )
urlpatterns = [
        path('', ListSnackView.as_view(), name = 'snack_list'),
        path('/home', ListSnackView.as_view(), name = 'snack_list'),
        path('/snacks_list', ListSnackView.as_view(), name = 'snack_list'),
        path('<int:pk>', DetailSnackView.as_view(), name = 'snack_detail'),
        path('create/', CreateSnackView.as_view(), name = 'snack_create'),
        path('delete/<int:pk>', DeleteSnackView.as_view(), name = 'snack_delete'),
        path('update/<int:pk>', UpdateSnackView.as_view(), name = 'snack_update'),
]