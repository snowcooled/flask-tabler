import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Tabler',
    version='0.0.1',
    url='http://github.com/snowcool/flask-tabler',
    license='BSD',
    author='Snow Cool',
    author_email='snowcooled@qq.com',
    description='An extension that includes Tabler in your '
    'project, without any boilerplate code.',
    long_description=read('README.rst'),
    packages=['flask_tabler'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'dominate',
        'visitor',
    ],
    classifiers=[
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
