<!-- base file upload handler classes, an the built-in concrete subclass -->

## UploadFileException(Exception)

## StopUpload(UploadFileException)
> [\__init__] if `connection_rest` is `True`, Django knows will halt the upload without consuming the rest off the upload. This will cause the browser to show a "connection rest" error.

## SkipFile(UploadFileException)
* this exception is raised by an upload handler that wants to skip a given file.

## StopFutureHandlers(UploadFileException)
* upload handlers that have handled a file and do not want future handlers to run should raise this exception instead of returning None.

## FileUploadHandler
> [\__init__] setup some necessary variable for later handling file.

> [\handle_row_input] handle the raw input from the client.

> [new_file] signal that a new file has been started.

> [receive_data_chunk] receive data from the streamed upload parser.

> [file_complete] signal that a file has completed. File size corresponds to the actual size accumulated by all the chunks.

> [upload_complete] signal that the upload is complete.

> [upload_interrupt] signal that the upload was interrupt.

## TemporaryFileUploadedHandler(FileUploadHandler)
* file upload handler to stream uploads into memory (used for small files)
> [new_file] create the tmp file by initiating a [django.core.files.uploadfile.TemporaryUploadedFile] object.

> [receive_data_chunk] just write the content into [self.file]

> [file_complete]

> [upload_interrupted] just close [self.file] and remove [self.file.temporary_file_path()]

## MemoryFileUploadHandler(FileUploadHandler)
* file upload handler to stream uploads into memory
> [handle_raw_input] check the content-length header to see if we should use memory handler (don't if the post is too large)

> [new_file] create the BytesIO file

> [receive_data_chunk] add the data to the BytesIO file.

> [file_complete] return the BytesIO file object if the handler is activated.

## load_handler
* given a path to a handler (such as above), return an instance of that handler
