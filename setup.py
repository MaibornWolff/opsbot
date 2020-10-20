import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


install_requires = [

]


setuptools.setup(
    name="opsbot",
    version="0.0.1",
    author="MaibornWolff",
    description="TODO Desc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="opsbot kubernetes dcos",
    license='Apache 2.0',
    url="https://github.com/MaibornWolff/opsbot/",
    packages=["app"],
    # packages=["opsbot", "dcosdeploy.commands", "dcosdeploy.adapters", "dcosdeploy.modules", "dcosdeploy.config", "dcosdeploy.util"],
    python_requires=">=3.7",
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'opsbot = app.main:main',
        ],
    }
)
