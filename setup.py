from setuptools import setup, find_packages

version = '2.0'

setup(
    name='mailman2',
    version=version,
    description='Mailman 2 API.',
    author='Adam Clark',
    author_email='adam@iris.washington.edu',
    url='http://github.com/iris-edu/mailman2',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
    zip_safe=False,
)
