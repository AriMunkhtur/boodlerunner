from django.contrib import admin
#from .forms import ReceiverForm
from .models import boodleReceiver
from .models import boodleRequest
from .models import boodleRunner
# Register your models here.
admin.site.register(boodleReceiver)
admin.site.register(boodleRunner)
admin.site.register(boodleRequest)

