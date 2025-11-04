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

class ApplicantNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email']

class JobNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = ApplicantNestedSerializer(read_only=True)
    job = JobNestedSerializer(read_only=True)
    applicant_id = serializers.PrimaryKeyRelatedField(queryset=Applicant.objects.all(), write_only=True, source='applicant')
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), write_only=True, source='job')

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'status', 'applied_on', 'applicant_id', 'job_id']

    def validate(self, data):
        applicant = data.get('applicant')
        job = data.get('job')
        if Application.objects.filter(applicant=applicant, job=job).exists():
            raise serializers.ValidationError('This applicant has already applied for this job.')
        return data