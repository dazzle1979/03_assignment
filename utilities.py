"""Module containing Utilities Class."""
import argparse
import os
import json
import time

class Utilities:
    """Utilities for week 3 assignment."""

    @classmethod
    def parse_arguments(cls):
        """Use argparse for commandline arguments."""
        parser = argparse.ArgumentParser(
            description = "Write CPU and Memory usage to json file."
        )
        parser.add_argument(
            "--stdout",
            help="Output data to stdout",
            action="store_true",
            required=False
        )
        parser.add_argument(
            "--no-cpu",
            help="Do not fetch, store or output cpu data",
            action="store_true",
            required=False
        )
        parser.add_argument(
            "--no-memory",
            help="Do not fetch, store or output memory data",
            action="store_true",
            required=False
        )
        return parser.parse_args()

    @classmethod
    def write_json(cls, data):
        """Write data to Json file."""
        timestamp = int(time.time())
        cls.ensure_dir("output")
        with open(f"./output/{timestamp}.json", "w") as data_file:
            json.dump(data, data_file, indent=4, sort_keys=True)

    @classmethod
    def ensure_dir(cls, directory):
        """Create directory if it not exists."""
        if not os.path.exists(directory):
            os.mkdir(directory)
