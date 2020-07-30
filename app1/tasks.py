from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .models import *

import random
import datetime

@shared_task
def testFillingModel():
    print("Start work testFillingModel")
    item = Test(
        name=f"It's random row, number - {random.random()}",
        date=datetime.datetime.now(),
    )
    item.save()