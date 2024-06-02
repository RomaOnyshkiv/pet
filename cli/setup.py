from setuptools import setup

setup(
    name="CLI",
    version='0.1',
    py_modules=['impl.remote', 'cli'],
    install_requires=[
        'click',
        'paramiko'
    ],
    entry_points='''
        [console_scripts]
        cli=cli:cli
    ''',
)