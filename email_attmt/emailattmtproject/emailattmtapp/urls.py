from django.urls import path
from emailattmtapp.views import EmailAttachementView

urlpatterns = [
    path('', EmailAttachementView.as_view(), name='emailattachment')

]