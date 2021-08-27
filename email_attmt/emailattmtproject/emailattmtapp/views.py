from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm
import socket
socket.getaddrinfo('localhost',port=22 )

class EmailAttachementView(View):
    form_class = EmailForm
    # template_name = 'emailattachment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'emailattchment.html', {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'emailattchment.html', {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except Exception as  e:
                return render(request, 'emailattchment.html', {'email_form': form, 'error_message': f'Either the attachment is too big or corrupt{e}'})

        return render(request, 'emailattchment.html', {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
