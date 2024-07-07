from django.core.mail import EmailMultiAlternatives
from django.db import connection
from django.utils.translation import get_language

from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from core.models import Setting

from epaper.models import EPaperEmail, GuestMessage
from epaper.forms import EPaperForm
# Create your views here.

class EPaperView(FormView):
    template_name = "epaper/epaper.html"

    form_class = EPaperForm
    success_url = '/epaper/thanks/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if not EPaperEmail.objects.filter(email=self.object.email):
            self.object.save()
            to = [self.object.email]
            self.send_mail(to)
        return super().form_valid(form)
    
    def send_mail(self, to):
        language =  get_language()
        setting =  Setting.objects.get(id=language)
        subject =f'您已成功訂閱 {setting.sitename} 電子報'
        text_content = f'您已成功訂閱 {setting.sitename} 電子報'
        html_content = f'<p>您已成功訂閱 {setting.sitename} 電子報</p>'
        msg = EmailMultiAlternatives(subject, text_content, None, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

class EPaperThanksView(TemplateView):
    template_name = "epaper/thanks.html"

class EPaperHomeDirectThanksView(TemplateView):
    template_name = "epaper/thanks.html"
    success_url = '/epaper/thanks/'
    def post(self, request, *args, **kwargs):
        email = request.POST['inputemail']
        #email = self.kwargs.get('email', '')
        if not EPaperEmail.objects.filter(email=email):
            EPaperEmail.objects.create(email=email)
            to = [email]
            self.send_mail(to)
        return render(request, self.template_name)
    
    def send_mail(self, to):
        language =  get_language()
        setting =  Setting.objects.get(id=language)
        subject =f'您已成功訂閱 {setting.sitename} 電子報'
        text_content = f'您已成功訂閱 {setting.sitename} 電子報'
        html_content = f'<p>您已成功訂閱 {setting.sitename} 電子報</p>'
        msg = EmailMultiAlternatives(subject, text_content, None, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

class ContactView(TemplateView):
    template_name = "epaper/contact.html"
    success_url = '/epaper/thanks/'
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        #email = self.kwargs.get('email', '')
        if not GuestMessage.objects.filter(email=email):
            GuestMessage.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, self.template_name)