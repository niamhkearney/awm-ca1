from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib import messages

from world import models
from world.forms import NewUser
from world.models import Profile, DogProfile
from world.forms import NewDog


def index(request):
    pass
    return render(request, 'base.html')


# Returns a list of dogs owned by the user for the dropdown menu in maps.html
@login_required()
def maps(request):
    if request.method == 'GET':
        dogcontext = DogProfile.objects.filter(owner=request.user)
        return render(request=request, template_name='map.html', context={'dogs': dogcontext})


@csrf_exempt
def register_request(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST.get("username")
            new_profile = Profile(user_id=user, username=username)
            new_profile.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUser()
    return render(request=request, template_name="registration/signup.html", context={"register_form": form})


# Updates the dogprofile where the dogid is equal to what was selected in the dropdown menu
# of map.html + the owner is the user
@login_required
def route_request(request):
    try:
        user = request.user
        if not user:
            raise ValueError("Can't get the user's details")

        point1 = request.POST.get('start', None)
        point1 = [float(part) for part in point1.split(",")]
        point1 = Point(point1, srid=4326)

        print(point1)

        point2 = request.POST.get('dest', None)
        point2 = [float(part) for part in point2.split(",")]
        point2 = Point(point2, srid=4326)

        print(point2)

        dog = DogProfile.objects.get(owner=user, id=request.POST.get('id'))
        dog.start = point1
        dog.dest = point2
        dog.save()

        return JsonResponse({"message": f"Set Location to {point1.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# For adding a new dog
@login_required
def newdog_request(request):
    if request.method == "POST":
        form = NewDog(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user
            dog.save()
            return redirect("home")
    form = NewDog()
    return render(request=request, template_name="dogform.html", context={"newdog_form": form})


# for displaying all the dogs the owner has in dogs.html

@login_required
def display_dogs(request):
    if request.method == 'GET':
        dogprofiles = DogProfile.objects.filter(owner=request.user)
        return render(request=request, template_name='dogs.html', context={'dogs': dogprofiles})
