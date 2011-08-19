import os, sys 
# Connect to Django to use models 
sys.path.append(os.path.expanduser('D:\dev\proj\invoycer')) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'invoycer.settings' 
# Pull in relevant models 
from invoycer.invoices.models import *