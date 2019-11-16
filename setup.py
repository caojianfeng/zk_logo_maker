#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: JeffreyCao
# Mail: jeffreycao1024@gmail.com
# Created Time:  2019-11-16 21:48:34
#############################################

from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="zk_logo_maker",
    version="1.0.0",
    keywords=("pip", "SICA", "featureextraction"),
    description="An feature extraction algorithm",
    long_description="An feature extraction algorithm, improve the FastICA",
    license="MIT Licence",

    url="https://github.com/JeffreyCao/zk_logo_maker",  # 项目相关文件地址，一般是github
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["pillow"]  # 这个项目需要的第三方库
)