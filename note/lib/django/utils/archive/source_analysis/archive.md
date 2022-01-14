## ArchiveException(Exception)
* base exception class for all archive errors.

## UnrecognizedArchiveFormat(ArchiveException)
* error raised when passed file is not a recognized archive format.

## extract
* unpack the tar or zip file at the specified path  to the directory specified by to_path

## Archive
* the external API class that encapsulates an archive implementation.

> [\__init__] ```self._archive = self._archive_cls(file)(file)```

> [\_archive_cls] (staticmethod)
* initiate the archive class base on file extension.

> [__enter__] ```return self```

> [__exit__] ```self.close()```

> [extra]
* extra the archive

> [list]
* list the archive

> [close]
* close the archive

## BaseArchive
* base archive class. Implementations should inherit this class.

> [\_copy_permission] (staticmethod)
* if the file in the archive has some permissions (this assumes a file won't be writable/executable without being readable), apply those permissions to the unarchived file.

> [split_leading_dir]
* split leading dir

> [has_leading_dir]
* return true if all the paths have the same leading path name.

> [target_filename]
* return the target filename

> [extract] ```raise NotImplementedError```

> [list] ```raise NotImplementError```

## TarArchive(BaseArchive)

> [\__init__]
* open that tar file

> [list]
* list that tar file

> [extract]
* extract that tar file

> [close]
* close that tar file

## ZipArchive(baseArchive)

> [\__init__]
* open that tar file

> [list]
* list that tar file

> [extract]
* extract that tar file

> [close]
* close that tar file

## extenion_map
* a mapping that map .tar, .tar.bz2, .tbz2, .tbz, .tz2, .tar.gz, .tgz, .tar.lzma, .tlz, .tar.xz, .txz to ```TarArchive``` and map .zip to ```ZipArchive```
