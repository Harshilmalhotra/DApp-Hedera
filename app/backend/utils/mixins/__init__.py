# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from urllib.parse import urlencode
from datetime import datetime, timedelta, date
import time
from decimal import *
from django.utils import timezone
import calendar

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import PermissionDenied

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import requests
import six
from pprint import pprint as pp
from djmoney.money import Money


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


def reCAPTCHAValidation(token):

	''' reCAPTCHA validation '''
	result = requests.post(
		'https://www.google.com/recaptcha/api/siteverify',
		 data={
		 	'secret': settings.RECAPTCHA_PRIVATE_KEY,
			'response': token
		 })

	return result.json()




def FormErrors(*args):
	'''
	Handles form error that are passed back to AJAX calls
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message




class AjaxFormMixinBase(object):
	'''
	Mixin to ajaxify django form - can be over written in view by calling form_invalid method
	'''
	
	def form_invalid(self, form):
		response = super(AjaxFormMixinBase, self).form_invalid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			return JsonResponse({'result': 'Error', "message": FormErrors(form), "redirect": False})
		return response



'''
Mixin to ajaxify django form - can be over written in view by calling form_valid method
'''
class AjaxFormMixin(AjaxFormMixinBase):
	
	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			form.save()
			return JsonResponse({'result': 'Success', 'message': "Thank you."})
		return response



class RecaptchaAjaxFormMixin(AjaxFormMixinBase):

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		response = super(RecaptchaAjaxFormMixin, self).form_valid(form)
		if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
			token = form.cleaned_data.get('recaptcha_token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				form.save()
				data = {'result': 'Success', 'message': "Thank you."}
				return JsonResponse(data)
			else:
				data = {'result': "Error", 'message': "There was an error, please try again"}
				return JsonResponse(data)
		return response
	


def recaptcha_form_submission(token):
	captcha = reCAPTCHAValidation(token)
	if captcha["success"]:
		return True
	return False



def RedirectParams(**kwargs):
	'''
	Used to append url parameters when redirecting users
	'''
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


def find_days(start:datetime, end:datetime, day:int)->list:
	days = (start + timedelta(days=i) for i in range((end - start).days + 1))
	day_list = [d for d in days if d.weekday() in [day] ]
	return day_list



def convert_money_to_tuple(money: Money)->tuple:
	return str(money.amount), str(money.currency)

def convert_tuple_to_money(money: tuple)->Money:
	amount = Decimal(money[0])
	currency = money[1]
	return Money(amount, currency)

def aware_now():
	return timezone.make_aware(datetime.now())

def aware_now_plus_trial():
	trial = datetime.now() + timedelta(days=settings.DEFAULT_PARTICIPANT_FREE_TRIALS)
	return timezone.make_aware(trial)

def last_day():
	today = datetime.now()
	weekday, day = calendar.monthrange(today.year, today.month)
	date_sting = f'{today.year}-{today.month}-{day}'
	return datetime.strptime(date_sting, '%Y-%m-%d')

def convert_datetime_to_aware(date):
	return timezone.make_aware(date)



def user_has_permissions_or_403(obj, **kwargs):
	user = kwargs.get("user")
	customer = kwargs.get("customer")
	account = kwargs.get("account")
	if user:
		if not obj.user == user:
			raise PermissionDenied()
	
	if customer:
		if not obj.customer == customer:
			raise PermissionDenied()
		
	if account:
		if not obj.account == account:
			raise PermissionDenied()
	return True
