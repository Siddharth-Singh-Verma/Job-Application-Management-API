from rest_framework import serializers
from .models import Applicant, Job, Application

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def validate(self, data):
        applicant = data.get('applicant')
        job = data.get('job')
        if Application.objects.filter(applicant=applicant, job=job).exists():
            raise serializers.ValidationError('This applicant has already applied for this job.')
        return data