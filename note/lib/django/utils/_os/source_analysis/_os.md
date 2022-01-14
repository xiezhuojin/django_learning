## safe_join
* join on or more path components to the base path component intelligently. return a normalized, absolute version of the final path.

## symlinks_supported
* return whether or not creating symlinks are supported in the host platform and/or if they are allowed to be created (e.g. on windows it requires admin permission)

## to_path
* convert value to pathlib.Path instance, if not already a Path.
