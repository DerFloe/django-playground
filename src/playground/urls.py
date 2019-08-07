from django.contrib import admin
from django.urls import path


from parcels.views import parcel_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parcels/',parcel_list_view)
]
