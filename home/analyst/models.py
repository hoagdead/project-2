from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hoc_sinh = models.BooleanField(default=False)
    is_giao_vien = models.BooleanField(default=False)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    lan_cuoi_dang_nhap = models.DateTimeField(auto_now=True)

# Create your models here.


class GiaoVien(models.Model):
    GIOI_TINH_CHOICES = [
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
    ]

    User = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    Ma_GV = models.CharField(max_length=20, unique=True)
    Ho_Ten = models.CharField(max_length=100)
    Gioi_tinh = models.CharField(max_length=10, choices=GIOI_TINH_CHOICES)
    SDT = models.CharField(max_length=15)
    Email = models.EmailField()
    Sinh_nhat = models.DateField()
    Dia_chi = models.TextField()
    Day_lop = models.ManyToManyField('LopHoc', blank=True)
    Chu_Nhiem = models.BooleanField(default=False)

class HocSinh(models.Model):
    GIOI_TINH_CHOICES = [
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
    ]

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    Ma_HS = models.CharField(max_length=20, unique=True)
    Ngay_sinh = models.DateField()
    Gioi_Tinh = models.CharField(max_length=10, choices=GIOI_TINH_CHOICES)
    Dia_chi = models.TextField()
    So_dt_bo_me = models.CharField(max_length=15)
    Lop = models.ForeignKey('LopHoc', on_delete=models.SET_NULL, null=True)
    Ngay_nhap_hoc = models.DateField()


class LopHoc(models.Model):
    Ten_lop_hoc = models.CharField(max_length=50)
    Khoi = models.CharField(max_length=10)
    Nien_Khoa = models.CharField(max_length=20)
    GV_Chu_Nhiem = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True, related_name='lop_chu_nhiem')
    Si_So = models.IntegerField()
    Tg_Tao = models.DateTimeField(auto_now_add=True)
    Tg_cap_Nhat = models.DateTimeField(auto_now=True)


class DiemSo(models.Model):
    LOAI_DIEM_CHOICES = [
        ('thuongxuyen', 'Thường xuyên'),
        ('giuaky', 'Giữa kỳ'),
        ('cuoiky', 'Cuối kỳ'),
    ]

    HS = models.ForeignKey(HocSinh, on_delete=models.CASCADE)
    Mon_hoc = models.ForeignKey('MonHoc', on_delete=models.CASCADE)
    GV = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    Loai_Diem = models.CharField(max_length=20, choices=LOAI_DIEM_CHOICES)
    Diem_so = models.FloatField()
    Ngay_nhap = models.DateField(auto_now_add=True)


class MonHoc(models.Model):
    Ma_mon_hoc = models.CharField(max_length=20, unique=True)
    Ten_Mon = models.CharField(max_length=100)
    He_So = models.FloatField()

class PhanCong(models.Model):
    Gv = models.ForeignKey(GiaoVien, on_delete=models.CASCADE)
    Lop = models.ForeignKey('LopHoc', on_delete=models.CASCADE)
    Mon = models.ForeignKey(MonHoc, on_delete=models.CASCADE)

class Backup(models.Model):
    tg_tao = models.DateTimeField(auto_now_add=True)
    duong_dan = models.FileField(upload_to='backups/')
    Kich_Thuoc = models.PositiveIntegerField()
    Note = models.TextField(blank=True)

class ThoiKhoaBieu(models.Model):
    NGAY_CHOICES = [
        ('thu2', 'Thứ 2'),
        ('thu3', 'Thứ 3'),
        ('thu4', 'Thứ 4'),
        ('thu5', 'Thứ 5'),
        ('thu6', 'Thứ 6'),
        ('thu7', 'Thứ 7'),
    ]

    Lop = models.ForeignKey('LopHoc', on_delete=models.CASCADE)
    Mon = models.ForeignKey(MonHoc, on_delete=models.CASCADE)
    GV = models.ForeignKey(GiaoVien, on_delete=models.CASCADE)
    Ngay = models.CharField(max_length=10, choices=NGAY_CHOICES)
    Tiet = models.IntegerField()

class HoatDong(models.Model):
    User = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    Hanh_dong = models.TextField()
    Thoi_Gian = models.DateTimeField(auto_now_add=True)

class LsChuyenLop(models.Model):
    HS = models.ForeignKey(HocSinh, on_delete=models.CASCADE)
    Lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    Ngay_bat_dau_hoc = models.DateField()
    Ngay_ket_thuc_hoc = models.DateField(null=True, blank=True)

class LsLenLop(models.Model):
    HS = models.ForeignKey('HocSinh', on_delete=models.CASCADE)
    Lop_cu = models.ForeignKey('LopHoc', on_delete=models.SET_NULL, null=True, related_name='lop_cu')
    Lop_moi = models.ForeignKey('LopHoc', on_delete=models.SET_NULL, null=True, related_name='lop_moi')
    Ngay_len_lop = models.DateField()
