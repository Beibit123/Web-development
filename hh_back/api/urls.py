from django.urls import path
from api.views import *


urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_item),
    path('companies/<int:company_id>/vacancies/', company_item_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_item),
    path('vacancies/top_ten/', vacancy_topten),
]