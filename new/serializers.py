from rest_framework import serializers
from .models import *


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('first_name', 'last_name', 'phone_number', 'email_address',
                  'region', 'city', 'level_of_education', 'id_type', 'id_number',
                  'are_you_employed', 'start_up_stages', 'start_up_name', 'number_of_founders', 'about_the_owner',
                  'full_month_dedication',)

#
