from django.shortcuts import render, get_object_or_404
from .models import Band
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Render the home page for the band application.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'band/homeband.html')

@login_required(login_url="user_auth:login")
def band_list(request):
    """
    Render a list of all bands.

    This view is protected and requires the user to be logged in.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered page displaying the list of bands.
    """
    list_of_bands = Band.objects.all()
    context = {'list_of_bands': list_of_bands}
    return render(request, 'band/bandlist.html', context)

def band_detail(request, pk):
    """
    Render the details of a specific band.

    Args:
        request: The HTTP request object.
        pk (int): The primary key of the band to retrieve.

    Returns:
        HttpResponse: The rendered page displaying the details of the specified band.
    """
    band = get_object_or_404(Band, pk=pk)
    context = {'band': band}
    return render(request, 'band/bandDetail.html', context)
