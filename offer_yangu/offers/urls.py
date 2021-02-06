
from .views import *
from rest_framework import routers

app_name = "offers"
router = routers.DefaultRouter()
router.register(r"offers", OffersViewset,basename="offers")
urlpatterns = router.urls + []
    # path('user/', UserRetrieveUpdateAPIView.as_view()),
    # path('verify/<str:token>', VerifyAPIView.as_view(), name='verify'),
    # path('users/email_sent', EmailSentAPIView.as_view(), name='email_password'),
    # path('users/password_reset', PasswordResetAPIView.as_view(), name='password_reset'),
    # path('social_auth/', SocialSignUp.as_view(), name="social_sign_up"),
