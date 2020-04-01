from django.urls import path
from.views import (api_def_cliente_view,api_create_cliente_view,api_delete_cliente_view,api_update_cliente_view)
app_name='api'

urlpatterns=[
    path('create/',api_create_cliente_view, name="create"),
    path("<name>/", api_def_cliente_view, name="detail"),
    path("<name>/update/",api_update_cliente_view, name="update"),
    path("<name>/delete/", api_delete_cliente_view, name="delete")
]