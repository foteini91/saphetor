
from django.contrib import admin
from django.urls import path
from saphetor_api.views import get_vcf_data, post_vcf_data , update_vcf_data, delete_vcf_data

urlpatterns = [
    path('data/', get_vcf_data),
    path('add_records/', post_vcf_data ),
    path('update_record/', update_vcf_data),
    path('delete_record/', delete_vcf_data)
    
    
]
