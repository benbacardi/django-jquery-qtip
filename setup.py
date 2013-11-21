from setuptools import setup

setup(
    name='django-jquery-qtip',
    version='2.1.1',
    url='https://github.com/benbacardi/django-jquery-qtip',
    description='jQuery qTip (http://qtip2.com) packaged in a django app to speed up new applications and deployment.',
    author='Ben Cardy',
    author_email='benbacardi@gmail.com',
    license='MIT',
    keywords='django jquery qtip staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['jquery_qtip'],
    package_data={'jquery_qtip': ['static/js/*.js', 'static/css/*.css',]},
    install_requires=['django-jquery >= 1.6',],
    include_package_data=True,
)
