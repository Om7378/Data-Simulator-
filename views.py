from django.shortcuts import render


def postgresql_settings(request):
    return render(request, 'postgresql.html')