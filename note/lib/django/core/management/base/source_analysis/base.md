## CommandError(Exception)
* exception class indicating a problem while executing a management command.

## SystemCheckError(CommandError)
* the system check framework detected unrecoverable errors.

## CommandParser(argparse.ArgumentParser)
* customized ArgumentParser class to improve some error messages and prevent SystemExit in several occasions, as SystemExit is unacceptable when a command is called programmatically.

## handle_default_options
* include any default options that all commands shoudl accept here so that ManagementUtility can handle them before searching for user commands.

## no_translations
* decorator that forces a command to run with translations deactivated.

## DjangoHelpFormatter(argparse.HelpFormatter)
* customized formatter so that command-specific arguments appear in the --help output before arguments common to all commands.

## OutputWrapper(io.TextIOBase)
* wrapper around stdout/stderr

## BaseCommand
* the base class from which all management commands ultimately derive.
* the `handle` method is typically the starting point for subclasses; many built-in commands and command types either place all of their logic in `handle`, ro perform some additional paring work in `handle` and then delegate from it to more specialized methods as needed.
> [\__init__] nothing special.

> [get_version] return the django version.

> [create_parser]
* create and return the `ArgumentParser` which will be used to parse the arguments to this command.

> [add_argument]
* entry point for subclassed commands to add custom arguments.

> [print_help]
* print the help message for this command

> [run_from_argv]
* set up any environment changes requests (e.g., Python path and Django settings), then run this command. If the command raises a `CommandError`, intercept it and print it sensibly to stderr. If the `--traceback` option is present or the raised `Exception` is not `CommandError`, raise it.

> [execute] basically call [self.handle].
* try to execute this command, performing system checks if needed. 

> [check]
* use the system check framework to validate entire Django project. 

> [check_migrations]
* print a warning if the set of migrations on disk don't match the migrations in the database.

> [handle] (IMPORTANT)
* the actual logic of the command. Subclasses must implement this method.

## AppCommand(BaseCommand)
* a management command which takes one or more installed application labels as arguments, and does something with each of them.

## LabelCommand(BaseCommand)
* a management command which takes one or more arbitrary arguments (labels) on the command line, and does something with each of them.
* rather than implementing `handle`, subclasses must implement `handle_label`, which will be called once for each label.
