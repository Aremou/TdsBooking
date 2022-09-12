from django.urls import path

from partenariats.views import partnerships_conditions, recap, request_partnerships

urlpatterns = [
    path('conditions-de-partenariat/', partnerships_conditions,
         name='partnerships-conditions'),
    path('demande-de-partenariat', request_partnerships,
         name="request-partnerships"),
    path('demande-de-partenariat/recapitulatif', recap,
         name="request-recap")
]
