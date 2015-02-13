import urllib
import time
import dateutil.parser
import dateutil.tz
import xml.etree.cElementTree as xml_parser
from django.utils.encoding import smart_unicode
from django.conf import settings 
from .models import Professor, Schedule, Location, Course

class CS50Client(object):


# Parse the xml once a day to get course data and save it to the database
# http://www.webmonkey.com/2010/02/integrate_web_apis_into_your_django_site/

