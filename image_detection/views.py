from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from django.conf import settings
import os

def detect_disability(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            image_path = instance.image.path
            model_path = 'v2_model_disability_detection.h5'
            model = load_model(model_path)
            img = image.load_img(image_path, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0
            predictions = model.predict(img_array)
            class_names = ['Blind', 'Deaf', 'Handicapped', 'Injured']
            predicted_class = class_names[np.argmax(predictions)]
            
            # Save predicted result to the database
            instance.predicted_result = predicted_class
            instance.save()
            
            return render(request, 'image_detection/result.html', {'instance': instance, 'predicted_class': predicted_class})
    else:
        form = ImageUploadForm()
    return render(request, 'image_detection/upload.html', {'form': form})

def home(request):
    # Fetch all uploaded images with predicted results
    uploaded_images = UploadedImage.objects.all()

    predictions = []
    for image_instance in uploaded_images:
        predictions.append({'instance': image_instance, 'predicted_class': image_instance.predicted_result})

    return render(request, 'image_detection/home.html', {'predictions': predictions})

def about(request):
    return render(request, 'image_detection/about.html')
