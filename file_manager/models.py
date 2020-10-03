import hashlib

from django.db import models


def get_file_path(instance, filename):
    """
    Get the file path
    :arg
    """

    def md5(f):
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

    hashed_filename = md5(instance.file.file)

    return f'{hashed_filename[:2]}/{hashed_filename}'


class File(models.Model):
    """
    Base file model
    :arg
    """
    file = models.FileField(upload_to=get_file_path)