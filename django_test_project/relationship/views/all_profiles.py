from django.shortcuts import render

from ..models import Profile


def all_profiles(request):
    profiles = Profile.objects.select_related("employee").all()

    return render(
        request,
        "relationship/all_profiles.html",
        {"profiles": profiles},
    )
