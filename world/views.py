import json

import overpy
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point, Polygon
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib import messages
from osgeo_utils.gdal2tiles import data

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


def petshop_locator(request):
    try:
        # Create overpass API object
        api = overpy.Overpass()

        b_box = request.POST.get("bbox", None)

        if b_box:
            bbox = b_box.split(",")
            shuffled_bbox = [bbox[1], bbox[0], bbox[3], bbox[2]]
            mod_bbox = [float(item) for item in shuffled_bbox]
            b_box = mod_bbox

        # finding petshops
        searchres = api.query(f"""
            [out:json][timeout:25];
            (
              node["shop"="pet"]{tuple(b_box)};
              way["shop"="pet"]{tuple(b_box)};
              relation["shop"="pet"]{tuple(b_box)};
            );
            out body;
            >;
            out skel qt;
            """)

        geojson_result = {
            "type": "FeatureCollection",
            "features": [],
        }

        nodes_in_way = []

        for way in searchres.ways:
            geojson_feature = {
                "type": "Feature",
                "id": "",
                "geometry": "",
                "properties": {}
            }
            poly = []
            for node in way.nodes:
                # Record the nodes and make the polygon
                nodes_in_way.append(node.id)
                poly.append([float(node.lon), float(node.lat)])

            try:
                poly = Polygon(poly)
            except:
                continue
            geojson_feature["id"] = f"way_{way.id}"
            geojson_feature["geometry"] = json.loads(poly.centroid.geojson)
            geojson_feature["properties"] = {}

            for k, v in way.tags.items():
                geojson_feature["properties"][k] = v

            geojson_result["features"].append(geojson_feature)

        # Process results that are 'nodes'
        for node in searchres.nodes:
            # Ignore nodes which are also in a 'way' as we will have already processed the 'way'.
            if node.id in nodes_in_way:
                continue
            geojson_feature = None
            geojson_feature = {
                "type": "Feature",
                "id": "",
                "geometry": "",
                "properties": {}
            }

            point = Point([float(node.lon), float(node.lat)])
            geojson_feature["id"] = f"node_{node.id}"
            geojson_feature["geometry"] = json.loads(point.geojson)
            geojson_feature["properties"] = {}
            for k, v in node.tags.items():
                geojson_feature["properties"][k] = v

            geojson_result["features"].append(geojson_feature)

            # Return the complete GeoJSON structure.
        return JsonResponse(geojson_result, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
