from django.shortcuts import render
from .models import Asset
from django.views import generic

# Create your views here.
class AssetManage(generic.ListView):
    template_name = "assets/asset_manage.html"
    context_object_name = "asset_list"
    
    def get_queryset(self):
        return Asset.objects.all()
    
        
def login(request):
    pass

def dashboard(request):
    pass

def asset_manage(request):
    asset_list = Asset.objects.all()
    return render(request, "assets/asset_manage.html", {
        "asset_list": asset_list,
    })


def host_manage(request, editing):
    pass

def asset_details(request, editing):
    pass

def history(request):
    pass

def rack_diagram(reqeust, editing):
    pass
