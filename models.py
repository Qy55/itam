from django.db import models

# Create your models here.

class IDC(models.Model):
    idc_name = models.CharField(max_length=15, primary_key=True)
    description = models.TextField()
    
class Rack(models.Model):
    idc_name = models.ForeignKey(IDC, on_delete=models.CASCADE)
    
    rack_name = models.CharField(max_length=10)
    rack_slot = models.IntegerField(default = 1)
    
    rack_indicator = models.CharField(max_length=20, primary_key=True)
    
class EquipGroup(models.Model):
    group_name = models.CharField(max_length=6, primary_key=True)
    description = models.TextField()
    
class Product(models.Model):
    product_name = models.CharField(max_length=64, primary_key=True)
    
    vendor = models.CharField(max_length=32)
    product_type = models.CharField(max_length=8)    
    
    cpu_socket = models.IntegerField()
    cpu_core_per_socket = models.IntegerField()
    
    network_port = models.IntegerField()
    
    
class Asset(models.Model):
    asset_code = models.CharField(max_length=20, primary_key=True)

    group_name = models.ForeignKey(EquipGroup, on_delete=models.CASCADE)
    idc_name = models.ForeignKey(IDC, on_delete=models.CASCADE)
    rack_indicator = models.ForeignKey(Rack, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    ext_network_port = models.IntegerField(default=0)
    
    
class Host(models.Model):
    host_name = models.CharField(max_length=32, primary_key=True)
    
    host_os = models.CharField(max_length=16)
    host_os_version = models.CharField(max_length=8)
    
    network_address = models.GenericIPAddressField()
    asset_code = models.ForeignKey(Asset, on_delete=models.CASCADE)
    

class ServiceGroup(models.Model):
    group_name = models.CharField(max_length=16, primary_key=True)
    description = models.TextField()
    
class ServiceProcess(models.Model):
    process_name = models.CharField(max_length = 32, primary_key=True)
    
    group_name = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE)
    host_name = models.ForeignKey(Host, on_delete=models.CASCADE)
    
    account_name = models.CharField(max_length=16)
    exec_path = models.TextField()
    exec_command = models.TextField()
    restart_command = models.TextField()

