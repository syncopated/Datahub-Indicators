import decimal

from django.db import models

class RoundingDecimalField(models.DecimalField):
	""" Accepts a float as a value, and rounds to a decimal with the proper
	number of decimal_places.
	"""
	def to_python(self, value):
		if value is None:
			return value
		try:
			if type(value) is float:
				value = str(round(value, self.decimal_places))
			return decimal.Decimal(value)
		except decimal.InvalidOperation:
			msg = self.error_messages['invalid'] % str(value)
			raise exceptions.ValidationError(msg)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^indicators\.fields\.RoundingDecimalField"])

class FileNameField(models.CharField):
    None
    
add_introspection_rules([], ["^indicators\.fields\.FileNameField"])
