# nuScenes dev-kit.
# Code written by Holger Caesar, 2018.

import argparse
import os

from tqdm import tqdm
from vqasynth.utils.io import exists, join_path

from nuscenes import NuScenes


def verify_setup(nusc: NuScenes):
    """
    Script to verify that the nuScenes installation is complete.
    """

    # Check that each sample_data file exists.
    print('Checking that sample_data files are complete...')
    for sd in tqdm(nusc.sample_data):
        file_path = join_path(nusc.dataroot, sd['filename'])
        assert exists(file_path), 'Error: Missing sample_data at: %s' % file_path

    # Check that each map file exists.
    print('Checking that map files are complete...')
    for map in tqdm(nusc.map):
        file_path = join_path(nusc.dataroot, map['filename'])
        assert exists(file_path), 'Error: Missing map at: %s' % file_path


if __name__ == "__main__":

    # Settings.
    parser = argparse.ArgumentParser(description='Test that the installed dataset is complete.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataroot', type=str, default='/data/sets/nuscenes',
                        help='Default nuScenes data directory.')
    parser.add_argument('--version', type=str, default='v1.0-trainval',
                        help='Which version of the nuScenes dataset to evaluate on, e.g. v1.0-trainval.')
    parser.add_argument('--verbose', type=int, default=1,
                        help='Whether to print to stdout.')

    args = parser.parse_args()
    dataroot = args.dataroot
    version = args.version
    verbose = bool(args.verbose)

    # Init.
    nusc_ = NuScenes(version=version, verbose=verbose, dataroot=dataroot)

    # Verify data blobs.
    verify_setup(nusc_)
