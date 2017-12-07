#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class DoctesetConan(ConanFile):
    name = "doctest"
    version = "1.2.6"
    url = "https://github.com/bincrafters/conan-doctest"
    description = "C++98/C++11 single header testing framework"
    license = "MIT"

    def source(self):
        source_url = "https://github.com/onqtam/doctest"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")
        #Rename to "sources" is a convention to simplify later steps

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src="sources")
        self.copy(pattern="*doctest.h*", dst="include", src=os.path.join("sources","doctest"))

    def package_id(self):
        self.info.header_only()
