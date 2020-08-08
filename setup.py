from distutils.core import setup

setup(
    name='quick_trade',
    version='2.1.2',
    packages=['quick_trade'],
    license='cc',
    description="trading system",
    url='https://github.com/VladKochetov007/quick_trade',
    long_description=open('README_for_pypi.txt').read(),
    install_requires=[
        'iexfinance',
        'numpy',
        'pandas',
        'plotly',
        'pykalman',
        'scikit-learn',
        'scipy',
        'ta',
        'tensorflow',
        'tqdm'
    ]
)
