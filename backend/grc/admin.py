from django.contrib import admin
from grc.models import Control, Policy, Evidence

# Register your models
admin.site.register(Control)
admin.site.register(Policy)
admin.site.register(Evidence)

#admin site username
#user: nim 
#password: 123