from django.db import models
"""import torch
from yolov7.detect import detect
from .forms import InputForm
# Create your models here.

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    #path = '\best.pt'
    #model = torch.hub.load("WongKinYiu/yolov7","custom",f"{path}",trust_repo=True)
    
    weights='\disaster_damage_detect\best.pt'
    conf=0.1 
    source='images/'
    detect(source=source, weights=weights,conf_thres=conf)


    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"""
