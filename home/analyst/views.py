from django.shortcuts import render
from analyst.models import GiaoVien, HocSinh, UserProfile, LopHoc, DiemSo, MonHoc, ThoiKhoaBieu, HoatDong




def home(request):
    SoHS = HocSinh.objects.count()
    SoGV = GiaoVien.objects.count()
    SoLop = LopHoc.objects.count()
    SoMon = MonHoc.objects.count()
    Hd = HoatDong.objects.count()
    context = {'SoHS': SoHS,
               'SoGV': SoGV,
               'SoLop': SoLop,
               'SoMon': SoMon,
                'Hd': Hd,
               }
    return render(request, 'home.html',context)