from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=200)
	defaultrate = models.DecimalField(max_digits=7, decimal_places=2)
	def __unicode__(self):
		return self.name
		
class Contact(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	salutation = models.CharField(max_length=5)
	email = models.EmailField()
	phone = models.CharField(max_length=13)
	def __unicode__(self):
		return "%s, %s" % (self.lastname, self.firstname)
		
class Client(models.Model):
	organization = models.ForeignKey(Organization)
	contact = models.ForeignKey(Contact)
	def __unicode__(self):
		if (self.organization):
			return "%s (%s)" % (self.contact, self.organization)
		else:
			return self.contact
			
class Project(models.Model):
	client = models.ForeignKey(Client)
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
		
class Invoice(models.Model):
	datecreated = models.DateTimeField('date created', editable=False, auto_now_add=True)
	datemodified = models.DateTimeField('date modified', editable=False, auto_now=True, blank=True, null=True)
	datefinalized = models.DateTimeField('date finalized', editable=False, blank=True, null=True)
	client = models.ForeignKey(Client)
	def __unicode__(self):
		return "%s (%s - %s)" % (self.client, self.datecreated, self.datefinalized)

class ExcludedProject(models.Model):
	invoice = models.ForeignKey(Invoice)
	project = models.ForeignKey(Project)
		
class Entry(models.Model):
	startdatetime = models.DateTimeField('start date/time', blank=True)
	enddatetime = models.DateTimeField('end date/time', blank=True)
	project = models.ForeignKey(Project)
	
	class Meta:
		verbose_name_plural = "entries"