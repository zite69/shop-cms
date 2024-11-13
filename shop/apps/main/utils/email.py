from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, engines
from django.utils.html import strip_tags
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from functools import lru_cache
from .urls import get_site_base_uri
import logging

def reset_template_cache():
    for engine in engines.all():
        engine.engine.template_loaders[0].reset()

logger = logging.getLogger('shop.apps.main.utils')

@lru_cache()
def logo_data():
    with open(finders.find('img/zite69_shop.png'), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo

@lru_cache()
def image_data(imgpath, imgcid):
    with open(finders.find(imgpath), 'rb') as f:
        image_data = f.read()
    image = MIMEImage(image_data)
    image.add_header('Content-ID', imgcid)
    return image

def send_waitlist_welcome(email):
    logger.debug(f"Called to send waitlist email to {email}")
    html_content = render_to_string("email/waitlist.html")
    text_content = strip_tags(html_content)

    message = EmailMultiAlternatives(
            subject="You have joined our waitlist!",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
    )

    message.mixed_subtype = 'related'
    message.attach_alternative(html_content, "text/html")
    message.attach(logo_data())

    #returns the number of messages sent. in this case should be either 1 or 0
    return message.send(fail_silently=False)

def send_email(email, **kwargs):
    # template = kwargs.get("template", "email/otp.html")
    # logo = kwargs.get("logo", False)
    # from_email = kwargs.get("from_email", settings.DEFAULT_FROM_EMAIL)
    # subject = kwargs.get("subject", "Your OTP to login to our site")
    # images = kwargs.get("images", {})
    # cc = kwargs.get("cc", [])
    # bcc = kwargs.get("bcc", [])
    # base_uri = kwargs.get("base_uri", get_site_base_uri())
    # kwargs['base_uri'] = base_uri
    kwargs = kwargs | ({
        "template": "email/otp.html",
        "logo": False,
        "from_email": settings.DEFAULT_FROM_EMAIL,
        "subject": "Your OTP to login to our site",
        "images": {},
        "cc": [],
        "bcc": [],
        "base_uri": get_site_base_uri(),
        "whatsapp_link": f"https://wa.me/{settings.WHATSAPP_NUMBER}"
        } | kwargs)
    template = kwargs.get("template")
    logo = kwargs.get("logo")
    from_email = kwargs.get("from_email")
    subject = kwargs.get("subject")
    images = kwargs.get("images")
    cc = kwargs.get("cc")
    bcc = kwargs.get("bcc")
 
    html_content = render_to_string(template, context=kwargs)
    # return html_content
    text_content = strip_tags(html_content)

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=[email]
    )
    if cc:
        message.cc = cc
    if bcc:
        message.bcc = bcc

    message.mixed_subtype = 'related'
    message.attach_alternative(html_content, "text/html")
    if logo:
        message.attach(logo_data())
    if images:
        for k in images:
            message.attach(image_data(k, images[k]))

    return message.send(fail_silently=False)

def send_email_otp(email, otp, **kwargs):
    return send_email(email, otp=otp, template="email/otp.html", subject="Your OTP to login to our site", **kwargs)

def send_email_verification(email, otp, **kwargs):
    return send_email(email, otp=otp, template="email/verification.html", subject="Verify your email address", **kwargs)

def send_email_invite(email, ctx):
    #Default context values
    def_ctx = {
        'template': 'email/invitation.html',
        'subject': 'You have been invited to join our site',
        'expiry': '7 days'
    }

    #Set defaults for context if they don't exist'
    for k in def_ctx:
        ctx.setdefault(k, def_ctx[k])

    return send_email(email, **ctx)

def send_email_seller_welcome(user, **kwargs):
    #Keeing the below commented out code in case we ever need to attach files to the email by default
    #We are currently linking to these images directly online rather than referring to the attachment in the 
    #mail template
    # kwargs = kwargs | ({
    #     "template": "email/welcome-paidseller.html", 
    #     "subject": "Welcome to zite69",
    #     "images": {
    #         "img/email/1-offline.jpg": "<1-offline>",
    #         "img/email/2-realtime.jpg": "<2-realtime>",
    #         "img/email/3-ecommerce.jpg": "<3-ecommerce>",
    #         "img/email/nl-logo.png": "<nl-logo>"
    #         }} | kwargs)
    kwargs = kwargs | ({
        "template": "email/welcome-paidseller.html",
        "subject": "Welcome to zite69",
        } | kwargs)
    kwargs['user'] = user

    return send_email(user.email, **kwargs)
