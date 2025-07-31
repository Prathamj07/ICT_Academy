from django.urls import path
## from test_app import home 
from test_app.views import home, dev, contact ##This is optimized


urlpatterns = [
    path('', home, name='home'), # Home page route
    path('dev.html', dev, name='dev'),
    path('contact.html', contact, name = 'contact'),
]
