from django.shortcuts import render, redirect
from .forms import PartnerCreate
from django.http import HttpResponse
from .models import Partner
#DataFlair

def index(request):
    saloon = Partner.objects.all()
    return render(request, 'saloons.html', {'saloon': saloon})


def upload(request):
    upload = PartnerCreate()
    if request.method == 'POST':
        upload = PartnerCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})


def update_partners(request, partners_id):
    partners_id = int(partners_id)
    try:
        partners_sel = Partner.objects.get(id = partners_id)
    except Partner.DoesNotExist:
        return redirect('index')
    partners_form = PartnerCreate(request.POST or None)
    if partners_form.is_valid():
       partners_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':partners_form})


def delete_partners(request, partners_id):
    partners_id = int(partners_id)
    try:
        partners_sel = Partner.objects.get(id = partners_id)
    except Partner.DoesNotExist:
        return redirect('index')
    partners_sel.delete()
    return redirect('index')