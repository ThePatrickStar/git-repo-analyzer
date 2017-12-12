from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.conf import settings
from django.shortcuts import render
import django

import os

from utils import *


def generate_commit_list(commits):

    settings.configure(
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'), ],
                # 'APP_DIRS': True,
            },
        ]
    )

    django.setup()

    danger(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'))

    context = {
        'commits': commits
    }

    print render(None, 'commit_list.html', context)

    with open('temp.html', 'w') as output_file:
        output_file.write(render_to_string('commit_list.html', context))



