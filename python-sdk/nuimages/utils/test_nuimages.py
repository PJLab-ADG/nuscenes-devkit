# nuScenes dev-kit.
# Code written by Holger Caesar, 2020.

import os
import unittest

from vqasynth.utils.io import open, exists, join_path, isdir

from nuimages import NuImages


class TestNuImages(unittest.TestCase):

    def test_load(self):
        """
        Loads up NuImages.
        This is intended to simply run the NuImages class to check for import errors, typos, etc.
        """

        assert 'NUIMAGES' in os.environ, 'Set NUIMAGES env. variable to enable tests.'
        nuim = NuImages(version='v1.0-mini', dataroot=os.environ['NUIMAGES'], verbose=False)

        # Trivial assert statement
        self.assertEqual(nuim.table_root, join_path(os.environ['NUIMAGES'], 'v1.0-mini'))


if __name__ == '__main__':
    unittest.main()
