from user.models import Profile
from django.forms.models import ModelForm

class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'first_name',
            'last_name',
            'gender',
            'address',
            'city',
            'pincode',
        ]