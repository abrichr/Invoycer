from invoices.models import *
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name information',
			{'fields':
				['salutation',
				'firstname',
				'lastname']
			}
		),
		('Contact information',
			{'fields':
				['email',
				'phone']
			}
		)
	]

admin.site.register(Organization)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Invoice)
admin.site.register(ExcludedProject)
admin.site.register(Entry)