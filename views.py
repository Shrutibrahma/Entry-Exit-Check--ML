from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import Student 
from .models import EntryExitTime
import easyocr
import keras_ocr
import base64
from PIL import Image
from io import BytesIO
import re
import time

@csrf_exempt
def getIndexPage(request):
    if request.method == 'POST':
        base64_image_data = request.POST['snapshotData']
        data=base64_image_data.split(',')
        base64_image_data=data[1]

        reader = easyocr.Reader(['en'])
        image_data = base64.b64decode(base64_image_data)
        image = Image.open(BytesIO(image_data))
        result = reader.readtext(image)
        extracted_text = ' '.join([entry[1] for entry in result])
        print("Extracted Text:", extracted_text)
        # Use a regular expression to find a sequence of 10 digits
        match = re.search(r'\b\d{10}\b', extracted_text)

        # Check if a match is found
        if match:
            # Extract the matched sequence
            extracted_number = match.group(0)
            print("Extracted Number:", extracted_number)
            data=EntryExitTime.objects.filter(stu=Student.objects.get(id=extracted_number)).order_by()
            print(data)
        else:
            print("No 10-digit number found.")
    return render(request,"index.html")