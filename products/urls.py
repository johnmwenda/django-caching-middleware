from django.conf.urls import url
from .views import ListCreateProductsView

app_name = 'products'
urlpatterns = [
    url(r'^products/', ListCreateProductsView.as_view(), name="products-list-create"),
    # path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),
    # path('auth/login/', LoginView.as_view(), name="auth-login"),
    # path('auth/register/', RegisterUsers.as_view(), name="auth-register")
]
