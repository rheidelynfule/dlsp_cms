from django.shortcuts import render
from .models import Page, SiteInfo, Department, Image


def index(request):
    school_name = SiteInfo.objects.get(title="school_name").value
    school = SiteInfo.objects.get(title="school").value
    address = SiteInfo.objects.get(title="address").value
    site = {"school_name": school_name,
            "address": address,
            "school": school, }
    home_info = Page.objects.get(title="Home").info
    admission_info = Page.objects.get(title="Admission").info
    programs_info = Page.objects.get(title="Programs").info
    about_info = Page.objects.get(title="About").info
    contactus_info = Page.objects.get(title="Contact Us").info
    image = Image.objects.get(name='home').image
    data ={
        "info": home_info,
        "school_name": school_name,
        "address": address,
        "school": school,
        "admission_info": admission_info,
        "programs_info": programs_info,
        "about_info": about_info,
        "contactus_info": contactus_info,
        }
    return render(request, 'index.html', {'data':data, 'site': site, 'image': image,})


def admission(request):
    school_name = SiteInfo.objects.get(title="school_name").value
    school = SiteInfo.objects.get(title="school").value
    address = SiteInfo.objects.get(title="address").value
    site = {"school_name": school_name,
            "address": address,
            "school": school, }
    image = Image.objects.get(name='admission').image
    admission_procedure = SiteInfo.objects.get(title='admission_procedure').value
    return render(request, 'admission.html', {'site': site, 'admission': admission_procedure, 'image': image})


def programs(request):
    school_name = SiteInfo.objects.get(title="school_name").value
    school = SiteInfo.objects.get(title="school").value
    address = SiteInfo.objects.get(title="address").value
    site = {"school_name": school_name,
            "address": address,
            "school": school, }
    image = Image.objects.get(name='programs').image
    departments = Department.objects.all()
    data = {
        "departments": departments,
    }
    return render(request, 'programs.html', {"data": data, 'site': site, 'image': image})


def about(request):
    school_name = SiteInfo.objects.get(title="school_name").value
    school = SiteInfo.objects.get(title="school").value
    address = SiteInfo.objects.get(title="address").value
    site = {"school_name": school_name,
            "address": address,
            "school": school, }
    image = Image.objects.get(name='about').image
    mission_info = SiteInfo.objects.get(title='mission').value
    vision_info = SiteInfo.objects.get(title='vision').value
    history_info = SiteInfo.objects.get(title='history').value
    data = {
        "mission_info": mission_info,
        "vision_info": vision_info,
        "history_info": history_info,
    }
    return render(request, 'about.html', {'site': site, 'data': data,'image': image})


def contactus(request):
    school_name = SiteInfo.objects.get(title="school_name").value
    school = SiteInfo.objects.get(title="school").value
    address = SiteInfo.objects.get(title="address").value
    site = {"school_name": school_name,
            "address": address,
            "school": school, }
    image = Image.objects.get(name='contactus').image
    contact_procedure = SiteInfo.objects.get(title='contact_procedure').value
    return render(request, 'contactus.html', {'site': site, 'contactus': contact_procedure, 'image': image})
