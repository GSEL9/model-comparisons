
import re
import os
import csv
import shutil

import numpy as np
import pandas as pd

from collections import OrderedDict


def write_final_results(path_to_file, results):
    """Write the total collection of results to disk."""

    if isinstance(results, pd.DataFrame):
        results.to_csv(path_to_file, columns=results.columns)
    else:
        data = pd.DataFrame([result for result in results])
        data.to_csv(path_to_file)

    return None


def setup_tempdir(tempdir, root=None):
    """Returns path and sets up directory if non-existent."""

    if root is None:
        root = os.getcwd()

    path_tempdir = os.path.join(root, tempdir)

    if not os.path.isdir(path_tempdir):
        os.mkdir(path_tempdir)

    return path_tempdir


def teardown_tempdir(path_to_dir):
    """Removes directory even if not empty."""

    shutil.rmtree(path_to_dir)

    return None


def read_prelim_result(path_to_file):
    """Read temporary stored results."""

    results = pd.read_csv(path_to_file, index_col=False)

    return OrderedDict(zip(*(results.columns, results.values[0])))


def write_prelim_results(path_to_file, results):
    """Store results in temporary separate files to prevent write conflicts."""

    with open(path_to_file, 'w') as outfile:
        writer = csv.DictWriter(
            outfile, fieldnames=list(results.keys()), lineterminator='\n'
        )
        writer.writeheader()
        writer.writerow(results)

    return None
