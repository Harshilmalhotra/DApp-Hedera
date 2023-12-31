# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path, re_path, include

# --------------------------------------------------------------
# app imports
# --------------------------------------------------------------
from users.views import AccountViewSet

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from hashgraphhub.routers import router

router.register('account', AccountViewSet)
urlpatterns = router.urls