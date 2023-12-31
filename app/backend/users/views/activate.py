# --------------------------------------------------------------
# Python imports
# -------------------------------------------------------------
import logging

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.conf import settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import AccountActivationTokenGenerator

logger = logging.getLogger(__name__)
account_activation_token = AccountActivationTokenGenerator()
User = get_user_model()

def activate(request, uidb64, token):

	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		next_url = request.GET.get("next")
		if next_url:
			return HttpResponseRedirect(next_url)
		logger.info(f"✅ Success users.activate() user = {user.email}")
		return redirect(settings.DJOSER["ACTIVATION_REDIRECT_URL"])
	else:
		logger.info(f"❌ Fail users.activate() user = {user.email}")
		return redirect(settings.DJOSER["ACTIVATION_REDIRECT_FAIL_URL"])
