
from .views import LocationsViewset, OffersViewset, CategoriesViewset, ReviewListCreateView
from rest_framework import routers
from django.urls import path

app_name = "offers"
router = routers.SimpleRouter()
router.register(r"offers", OffersViewset, basename="offers")
router.register(r"offer_categories", CategoriesViewset, basename="category")
router.register(r"locations", LocationsViewset, basename="location")
urlpatterns = [
 path('offers/<id>/reviews/', ReviewListCreateView.as_view(),  name='offer_reviews'),
] + router.urls


# path('user/', UserRetrieveUpdateAPIView.as_view()),
# path('verify/<str:token>', VerifyAPIView.as_view(), name='verify'),
# path('users/email_sent', EmailSentAPIView.as_view(), name='email_password'),
# path('users/password_reset', PasswordResetAPIView.as_view(), name='password_reset'),
# path('social_auth/', SocialSignUp.as_view(), name="social_sign_up"),
