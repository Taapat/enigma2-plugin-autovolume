# -*- coding: utf-8 -*-

from distutils.core import setup


setup(name='enigma2-plugin-systemplugins-autovolume',
	version='1.0',
	author='Taapat',
	author_email='taapat@gmail.com',
	package_dir={'SystemPlugins.AutoVolume': 'src'},
	packages=['SystemPlugins.AutoVolume'],
	description='Simple automatic volume adjustment',
	)
