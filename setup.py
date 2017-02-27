from distutils.core import setup

setup(
    name='requirements-tree',
    version='1.0.0',
    packages=['', 'src', 'src.tree', 'src.compile'],
    url='https://github.com/ShamsNarsinh/requirements-tree.git',
    license='MIT',
    author='Shams Narsinh',
    author_email='shams.aryans@gmail.com',
    description='Generate pip package dependency tree using requirements.txt',
    entry_points={
            'console_scripts': [
                'requirements-tree=requirements-tree.__main__:main',
            ]
        }
)
