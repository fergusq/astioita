from typing import Any, Callable

import re

NonEmptyString = lambda x: re.fullmatch(r'.+', x)
Key = lambda x: re.fullmatch(r'\d+', x)

class Column:
	def __init__(self, name_en: str, name_fi: str, validator: Callable[[str], Any], parser: Callable[[str], Any] = lambda x: x) -> None:
		self.name_en = name_en
		self.name_fi = name_fi
		self.validator = validator
		self.parser = parser
    
	def validate(self, form: Any) -> bool:
		return bool(self.validator(form[self.name_fi]))
	
	def set_from_form(self, obj: Any, form: Any) -> None:
		str_rep = self.parser(form[self.name_fi])
		setattr(obj, self.name_en, str_rep)