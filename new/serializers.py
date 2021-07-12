from rest_framework import serializers
from .models import *


class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'phone_number', 'email_address',
                  'name_of_school', 'year', 'course', 'programming_language_name',
                  'framework_name',)


#
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolName
        fields = ('name_of_university',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = ('programming_language_name',)


class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = ('framework_name', 'language_of_framework',)
