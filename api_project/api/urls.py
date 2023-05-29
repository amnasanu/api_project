from django.urls import path
from api.views import store_input_data, get_input_data

urlpatterns = [
    path('store-data/', store_input_data, name='store_input_data'),
    path('get-data/', get_input_data, name='get_input_data'),
]
