# -*- coding: utf-8 -*-
"""
    PyValitron
    ~~~~~~
    Python Inputs Validation Library
    :copyright: (c) 2016 by Clivern (hello@clivern.com).
    :license: MIT, see LICENSE for more details.
"""


class Validator(object):

    _input = None
    _errors = {}
    _required = False

    def set_input(self, input_value):
        self._input = input_value

    def required(self):
        pass

    def lenght_between(self, from_lenght, to_lenght):
        if int(to_lenght) > len(self._input) > int(from_lenght):
            return True
        else:
            return False

    def min_length(self, min_lenght):
        if len(self._input) >= int(min_lenght):
            return True
        else:
            return False

    def max_length(self, max_length):
        if len(self._input) <= int(max_length):
            return True
        else:
            return False

    def exact_length(self, exact_length):
        if len(self._input) == int(exact_length):
            return True
        else:
            return False

    def greater_than(self, number):
        if int(self._input) > int(number):
            return True
        else:
            return False

    def greater_than_equal(self, number):
        if int(self._input) >= int(number):
            return True
        else:
            return False

    def less_than(self, number):
        if int(self._input) < int(number):
            return True
        else:
            return False

    def less_than_equal(self, number):
        if int(self._input) <= int(number):
            return True
        else:
            return False

    def equal(self, number):
        if int(self._input) == int(number):
            return True
        else:
            return False

    def email(self):
        pass

    def emails(self, sep=','):
        pass

    def url(self, protocols=['http', 'https'], relative = False):
        pass

    def ip(self, formats=['ipv4', 'ipv6']):
        if 'ipv4' in formats and 'ipv6' in formats:
            return self.ipv4() and self.ipv6
        elif 'ipv4' in formats:
            return self.ipv4()
        elif 'ipv6' in formats:
            return self.ipv6()
        else:
            return False

    def ipv4(self):
        parts = self._input.split('.')
        if len(parts) == 4 and all(x.isdigit() for x in parts):
            numbers = list(int(x) for x in parts)
            return all(num >= 0 and num < 256 for num in numbers)
        return False

    def ipv6(self):
        parts = self._input.split(':')
        if len(parts) > 8:
            return False

        num_blank = 0
        for part in parts:
            if not part:
                num_blank += 1
            else:
                try:
                    value = int(part, 16)
                except ValueError:
                    return False
                else:
                    if value < 0 or value >= 65536:
                        return False

        if num_blank < 2:
            return True
        elif num_blank == 2 and not parts[0] and not parts[1]:
            return True
        return False

    def alnum(self, options):
        pass

    def integer(self):
        pass

    def numeric(self):
        pass

    def decimal(self):
        pass

    def matches(self, regex, flags=0):
        if isinstance(regex, string_types):
            regex = re.compile(regex, flags)

        if regex.match(self._input):
            return True
        else:
            return False

    def alpha(self):
        pass

    def alpha_numeric(self):
        pass

    def alpha_dash(self):
        pass

    def base64(self):
        pass

    def get_errors(self):
        """Get a list of errors"""
        return self._errors

    def errors_exist(self):
        """Check if errors exist"""
        return True if len(self._errors) > 0 else False

    def clear_errors(self):
        """Clear all catched errors"""
        self._errors = {}

    def _set_error(self, vrule, error):
        """Set catched error"""
        if vrule == '' or error == '':
            return False
        else:
            self._errors[vrule] = error
        return True