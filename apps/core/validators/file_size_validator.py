from django.core.exceptions import ValidationError


def file_size_checker(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File size is too large. Size should not exceed 5 MiB.')
