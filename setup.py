from setuptools import setup

setup(
    name='huawei_lte_rest_api',
    packages=['huawei_lte_rest_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-cors',
        'huawei-lte-api',
    ],
)
