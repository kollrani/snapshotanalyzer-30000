from setuptools import setup

setup(
    name='snapshoalyzer-30000',
    version='0.1',
    author="AnuK",
    author_email="kolluriap@gmail.com",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/kollrani/snapshotanalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
