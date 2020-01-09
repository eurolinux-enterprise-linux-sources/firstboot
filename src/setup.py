#!/usr/bin/python2

from distutils.core import setup
from glob import *
import os

data_files = [('/usr/sbin', ['progs/firstboot']),
              ('/etc/rc.d/init.d', ['init/firstboot']),
              ('/usr/share/firstboot/themes/default',
               glob('themes/default/*.png')),
              ('/usr/share/firstboot/modules', glob('modules/*.py'))]

# add the firstboot start script for s390 architectures
if os.uname()[4].startswith('s390'):
    data_files.append(('/etc/profile.d', ['scripts/firstboot.sh']))
    data_files.append(('/etc/profile.d', ['scripts/firstboot.csh']))

setup(name='firstboot', version='1.110',
      description='Post-installation configuration utility',
      author='Chris Lumens', author_email='clumens@redhat.com',
      url='http://fedoraproject.org/wiki/FirstBoot',
      data_files=data_files,
      packages=['firstboot'])
