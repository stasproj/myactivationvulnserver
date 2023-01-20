from django.shortcuts import render
from .models import Keys
from django.http import JsonResponse

def KeyPanel(request):
    action = request.GET.get('action', 'Default')
    key = request.GET.get('key', 'Default')
    if action == "delete":
        Keys.objects.filter(Key=key).delete()
    elif action == "add":
        add_key = Keys(Key=key)
        add_key.save()
    return render(request, 'index.html')
def iskeyvalid(request):
    key = request.GET.get('key', 'Default')
    if Keys.objects.filter(Key=key):
        return JsonResponse({"valid":"true"})
    else:
        return JsonResponse({"valid":"false"})
