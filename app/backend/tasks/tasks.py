# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.storage import staticfiles_storage

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from celery import shared_task
from celery.utils.log import get_task_logger

User = get_user_model()
 
logger = get_task_logger(__name__)


@shared_task(bind=True)
def create_email(self, **kwargs):
    '''
    Used to create an email and send via a selection of templates
    '''
    subject = kwargs.get("subject", "")
    template = kwargs.get("template")
    cc_email = kwargs.get("cc_email", [])
    context = kwargs.get("context", {})
    bcc_email = kwargs.get("bcc_email", [])
    user_id = kwargs.get("user_id")
    internal = kwargs.get("internal", False)
    message = kwargs.get("message")
    signature = kwargs.get("signature")

    username = kwargs.get("username",settings.EMAIL_HOST_USER )
    password = kwargs.get("password",settings.EMAIL_HOST_PASSWORD )
    display_name = kwargs.get("display_name", settings.DISPLAY_NAME)
    
    match internal:
        case False:
            try:
                user = User.objects.get(id=user_id)
                email = user.email
                context["email"] = email
                context["full_name"] = user.get_full_name()
            except User.DoesNotExist:
                return f"Task: Send email to [{email}]: Fail - User does not exist"
        case True:
            email =settings.EMAIL_HOST_USER
    if signature:
        context["coach_full_name"] = signature
    if message:
        context["message"] = message
    
    site_id = settings.SITE_ID
    current_site = Site.objects.get(id = site_id).domain
    if settings.PRODUCTION:
        protocol = "https://"
    else:
        protocol = "http://"
    context["domain"] = f'{protocol}{current_site}'
    context["support_email"] = settings.EMAIL_HOST_USER
    context["logo"] = 'https://pns.ams3.digitaloceanspaces.com/static/branding/logo_150.png' 
 
    html_content = render_to_string(template, context ) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
 
    with get_connection(
            host= settings.EMAIL_HOST,
            port= settings.EMAIL_PORT,
            username=username,
            password=password,
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                f'{display_name} <{username}>',
                [email],
                cc=cc_email,
                bcc=bcc_email,
                connection=connection)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    return f"Task: Send email to [{email}]: Success"