#!/bin/env python
import os
import OpenImageIO as oiio

package_version = os.environ["REZ_OIIO_VERSION"]
assert package_version == oiio.VERSION_STRING, f"Expected: {package_version}, Got: {oiio.VERSION_STRING}"

