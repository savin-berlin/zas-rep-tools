#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Corpus Module
# Author:
# c(Developer) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######


import platform
from raven import Client



#self.client.captureException()


def initialisation():
    platform_info = {"platform":platform.platform(), "uname":platform.uname(), "system":platform.system(), "processor":platform.processor(), "machine":platform.machine(), "version":platform.version(), "architecture":platform.architecture  }
    python_info = {"python_build":platform.python_build(), "python_compiler":platform.python_compiler(),  "python_implementation":platform.python_implementation(), "python_version":platform.python_version(), }
    user_info = {"platform_info":platform_info, "python_info":python_info}
    client = Client(dsn='https://0ec650403a06441aa6075e14322a9b15:ba5a980db0064f25b118d724eeb4d877@sentry.io/1213596',

            include_paths=[__name__.split('.', 1)[0]],
            release = '0.1',
            user_info = user_info,
            #intern_attribute = self.__dict__,
            ignore_exceptions = [
            'Http404'
            ],
            processors = (
            'raven.processors.SanitizePasswordsProcessor',
            ),

            # pass along the version of your application
            # release='1.0.0'
            # release=raven.fetch_package_version('my-app')
            #release=raven.fetch_git_sha(os.path.dirname(__file__)),
            )
    return client