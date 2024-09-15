from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['photo', 'first_name', 'last_name', 'email', 'mobile', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            img = Image.open(photo)
            
            if img.mode != 'RGB':
                img = img.convert('RGB')

            img.thumbnail((140, 140))  # Resize image
            output = BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)

            # Return the new image file
            return InMemoryUploadedFile(
                output, 'ImageField', f"{photo.name.split('.')[0]}.jpg", 
                'image/jpeg', output.getbuffer().nbytes, None
            )
        return photo
