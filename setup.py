from setuptools import setup

setup(
    name='snapshot-analyzer',
    version='0.1',
    packages=[''],
    url='https://github.com/pradeepnprasad/shotty',
    license='GPLv3+',
    author='pradeepnprasad',
    author_email='',
    description='snapshot-analyzer from acloudguru to manage ec2 instances',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)
