from setuptools import setup

setup(
    name='@monorepo-flask-react/server',
    packages=['server'],
    include_package_data=True,
    install_requires=['flask']
)