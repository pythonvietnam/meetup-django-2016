from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
from django.conf import settings
from .forms import CareerForm
from .models import Career


class CareerViews(View):
  html_mail = """
      <h3>INFO<h3>
      <div>
        <p><strong>Full name</strong> : <span>$FULLNAME<span></p>
        <p><strong>Birthday</strong> : <span>$BIRTHDAY<span></p>
        <p><strong>Gender</strong> : <span>$GENDER<span></p>
        <p><strong>Email</strong> : <span>$EMAIL<span></p>
        <p><strong>Phone</strong> : <span>$PHONE<span></p>
        <p><strong>Address</strong> : <span>$ADDRESS<span></p>
        <p><strong>Attachments</strong> : <span>$ATTACHMENTS<span></p>
        <p><strong>Datetime</strong> : <span>$DATETIME<span></p>
      </div>

  """

  @staticmethod
  def submitform(request):
    form = CareerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      subject = "%s send CV" % request.POST.get('fullname', '')
      from_email = request.POST.get('email', '')
      to = settings.EMAIL_TO
      html_content = CareerViews.get_html_email(request.POST, request.FILES)

      attachment = request.FILES['attachment']
      filename = attachment.name

      msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
      msg.attach(filename=filename, content=attachment.read(), mimetype=attachment.content_type)
      msg.content_subtype = "html"
      msg.send()

      instance = form.save(commit=False)
      instance.save()
      return redirect('/form/sent/')

    return render(request, 'form.html', {'form': form})


  @staticmethod
  def get_html_email(post_value, file_value):
    fullname = post_value.get('fullname', '')
    birthday = post_value.get('birthday', '')
    gender = post_value.get('gender', '')
    email = post_value.get('email', '')
    phone = post_value.get('phone', '')
    address = post_value.get('address', '')
    date_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    attachments = file_value['attachment'].name
    html = CareerViews.html_mail.replace('$FULLNAME', fullname) \
      .replace('$BIRTHDAY', birthday) \
      .replace('$GENDER', gender) \
      .replace('$EMAIL', email) \
      .replace('$PHONE', phone) \
      .replace('$ADDRESS', address) \
      .replace('$ATTACHMENTS', attachments) \
      .replace('$DATETIME', date_time)
    return html

  @staticmethod
  def submitform_sent(request):
    return render(request, 'form_success.html')
