# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.core.management.base import BaseCommand
from bims.management.commands.update_boundary import (
    UpdateBoundary
)


class Command(UpdateBoundary, BaseCommand):
    help = 'Import provinces from shp file'

    def handle(self, *args, **options):
        print(os.path.join(
            settings.STATIC_ROOT,
            'data/province/province_boundary.shp'
        ))
        self.save_data(
            os.path.join(
                settings.STATIC_ROOT,
                'data/province/province_boundary.shp'
            ),
            'province', 'provname')
