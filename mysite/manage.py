#!/usr/bin/env python
import os
import sys
# import socketMethod

if __name__ == "__main__":
    # socketMethod.socketMethod()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
