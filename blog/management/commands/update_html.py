from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.loader import get_template
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Update HTML template with current date and time'

    def handle(self, *args, **kwargs):
        # Get the path to the HTML template file
        template_path = os.path.join(settings.BASE_DIR, 'blog', 'templates', 'blog', 'post_list.html')

        # Get the template
        template = get_template(template_path)

        # Render the template with the current date and time
        rendered_html = template.render({'current_datetime': timezone.now()})

        # Write the rendered HTML back to the file
        with open(template_path, "w") as file:
            file.write(rendered_html)

        self.stdout.write(self.style.SUCCESS('HTML template updated successfully!'))


"""To run this management command, you would execute:

          python code:          python manage.py update_html

This command will read your index.html template, update it with the current date and time, and then
save the changes back to the file. Additionally, it will display a success message indicating that 
the HTML template has been updated.

Remember to replace "index.html" with the path to your actual HTML template file. You can place this
management command in any app within your Django project."""