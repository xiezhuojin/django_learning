<!-- classes representing uploaded files -->
## UploadFile(django.core.files.base.File)
* an abstract uploaded file (`TemporaryUploadedFile` and `InMemoryUploadedFile` are the built-in concrete subclasses). An `UploadedFile` object behaves somewhat like a file object and represents some file data that the user submitted with a form.

> [\_set_name] just use the basename of the file -- anything else is dangerous

## TemporaryUploadedFile(UploadedFile)
* a file uploaded to a temporary location (for example: /tmp/upload)

## InMemoryUploadedFile(UploadFile)
* a file uploaded into memory

> [\__init__] just adds an additional [field_name] parameter, beside these is nothing special then [UploadedFile]

> [open] seek to the beginning, then return itself.

> [chunks] seek to the beginning, yield [self.read()]

## SimpleUploadedFile(InMemoryUploadedFile)
* a simple representation of a file, which just has content, size, and a name.

> [from_dict] return a [SimpleUploadedFile] object from a dictionary with keys (filename, content-type, content)
