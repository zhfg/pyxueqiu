import setuptools

setuptools.setup(
    name="pyxueqiu",
    version="0.0.1",
    author="jacob",
    author_email="angell.zhfg@gmail.com",
    description="package for read data from xueqiu",
    long_description="package for read data from xueqiu",
    long_description_content_type="text/markdown",
    url="https://github.com/zhfg/pyxueqiu",
    project_urls={
        "Bug Tracker": "https://github.com/zhfg/pyxueqiu/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)