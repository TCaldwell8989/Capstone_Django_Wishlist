from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, VisitedForm

def place_list(request):

    """ If this is a POST request, the user clicked the ADD button
    in the form. Check if the new place is valid, if so, save a
    new Place to the database, and redirect to this same page.
    This creates a GET request to this same route.

    If not a POST route, or Place is not valid, display a page
    with a list of places and a form to add a new place.
    """

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save() # create a new place object from the form
        if form.is_valid(): # checks for DB constraints violated
            place.save()    # Saves the place to the db
            # Redirect to a GET request for this same route
            return redirect('place_list')


    places = Place.objects.order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html',
                  {'places': places, 'new_place_form': new_place_form})

# Display a page of places visited
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

# Update the database and save update
def place_is_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = Place.objects.get(pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')

# get a row of data about a place from the database
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'travel_wishlist/place_detail.html', {'place': place})

# Edit a place as visited with a user review and date visited
def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = VisitedForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.visited = True
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = VisitedForm(instance=place)
    return render(request, 'travel_wishlist/place_edit.html', {'form': form, 'place': place})