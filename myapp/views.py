import http
from django.shortcuts import  render,HttpResponse
from myapp.models import Files, Locations
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import math
import numpy as np

# Create your views here.
def homeview(request):
    dc = Locations.objects.all().values();
    dc = Locations.objects.get(ULPIN='7DH2MKD77DEJFL');
    print(str(dc.latitude)+ " "+ str(dc.longitude));
    return render(request,"index.html")


def upload(request):
    if request.method == 'POST':
        file2= request.FILES['file']
        document = Files.objects.create(file=file2)
        document.save()
        
        # dc=UploadFiles.objects.get(id=)
    # if request.method == 'POST' and request.FILES['file']:
    #     upload = request.FILES['file']
    #     fss = FileSystemStorage()
    #     file = fss.save(upload.name, upload)
    #     file_url = fss.url(file)
        return HttpResponse("Your file was Saved")
    return render(request, "index.html")


def create(request):
    if request.method == 'POST':
        dist=request.POST['district']
        lat=request.POST['latitude']
        long =request.POST['longitude']
        #latitude
        x1=math.trunc(float(lat)) 
        x2=x1+90
        z1=np.base_repr(x2,base=14)
        a1=int((str(lat).split('.')[1][0]))
        a2=int(str(lat).split('.')[1][1])
        a3=int(str(lat).split('.')[1][2])
        x3 = int(str(a1) + str(a2) + str(a3))
        z2=np.base_repr(x3,base=32)
        a4=int(str(lat).split('.')[1][3])
        a5=int(str(lat).split('.')[1][4])
        a6=int(str(lat).split('.')[1][5])
        x4 = int(str(a4) + str(a5) + str(a6))
        z3=np.base_repr(x4,base=32)
        #longitude
        y1=math.trunc(float(long)) 
        y2=y1+180
        z4=np.base_repr(y2,base=19)
        b1=int((str(long).split('.')[1][0]))
        b2=int(str(long).split('.')[1][1])
        b3=int(str(long).split('.')[1][2])
        x5 = int(str(b1) + str(b2) + str(b3))
        z5=np.base_repr(x5,base=32)
        b4=int(str(long).split('.')[1][3])
        b5=int(str(long).split('.')[1][4])
        b6=int(str(long).split('.')[1][5])
        x6 = int(str(b4) + str(b5) + str(b6))
        z6=np.base_repr(x6,base=32)
        x7=501
        z7=np.base_repr(x7,base=32)
        z=z1+z2+z3+z4+z5+z6+z7
        data= Locations.objects.create(district=dist,latitude=lat,longitude=long,ULPIN=z)
        data.save()
        return HttpResponse("ULPIN Created")
    return render(request,"index.html")    


def ulpin(request):
    if request.method == 'POST':
        ulpin2 = request.POST['ulpin']
        try:
            ulpin=Locations.objects.get(ULPIN=ulpin2)
            return render(request, 'ulpin.html',{'ulpin': ulpin}) 
        except ObjectDoesNotExist:
            return render(request, 'index.html')
            
    return render(request, 'index.html')
        # return HttpResponse(ulpin.district)
        