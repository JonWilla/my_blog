
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line

        # Import your management command
        from blog.management.commands.update_html import Command as UpdateHtmlCommand

        # Add your management command to the COMMANDS dictionary
        COMMANDS = {
            'update_html': UpdateHtmlCommand(),
        }

        # Update the COMMANDS dictionary with the default Django commands
        COMMANDS.update({
            'help': 'django.core.management.commands.help',
            'version': 'django.core.management.commands.version',
            'startapp': 'django.core.management.commands.startapp',
            'startproject': 'django.core.management.commands.startproject',
            # Add other default commands as needed
        })

        # Execute the management command
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()






















# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
