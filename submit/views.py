from django.shortcuts import render
from .forms import InputForm
import random
import numpy as np
import os
import sys
import torch
import cv2
import logging
from yolov7 import *
# Create your views here.
def submit(request):
    context ={}
    context['form']= InputForm()
    return render(request, "submit.html", context)
def image(request):
    if request.method == 'POST':
            form = InputForm(request.POST, request.FILES)
            if form.is_valid():
                # Get the uploaded image from the forms
                uploaded_image = request.FILES['image']
                save_dir = os.path.join(os.path.dirname('disaster_damage_detection'), 'static')
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                
                # Construct the path to save the uploaded image
                save_path = os.path.join(save_dir, uploaded_image.name)
                
                # Save the uploaded image to the specified directory
                with open(save_path, 'wb') as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)
                os.system('cmd /c "py yolov7\\detect.py --weights best.pt --conf 0.1 --source static\\"')
                #detected_dir=os.path.join('runs', 'detect')
                #detected_dir=os.path.join(detected_dir, 'exp')
                #detected_image=os.path.join(detected_dir, uploaded_image.name)
                # Pass the detection results to the template for display
                return render(request, 'image.html', {'image': uploaded_image})
    else:
        form = InputForm()
        return render(request, 'submit.html', {'form': form})