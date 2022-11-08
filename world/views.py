from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib import messages

from world import models
from world.forms import NewUser
from world.models import Profile


def index(request):
    pass
    return render(request, 'base.html')


def maps(request):
    pass
    return render(request, 'map.html')


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


@login_required
def location_request(request):
    try:
        user_profile = request.user.profile
        if not user_profile:
            raise ValueError("Can't get the user's details")

        point = request.POST.get('point', None)
        point = [float(part) for part in point.split(",")]
        point = Point(point, srid=4326)

        user_profile.location = point
        user_profile.save()

        return JsonResponse({"message": f"Set Location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
