from django.shortcuts import render

from .models import Parcel

# Create your views here.

def parcel_list_view(request):
    parcel_objects = Parcel.objects.all()
    context = {
        'parcel_objects': parcel_objects
    }
    return render(request, "parcels/index.html", context)