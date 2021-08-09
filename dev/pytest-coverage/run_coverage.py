"""
A script for running path
"""
import os
import subprocess
from pathlib import Path


import subprocess

test_failed = False
try:
    grepOut = subprocess.check_output(
        "pytest --cov=textdescriptives --cov-config=dev/pytest-coverage/.coveragerc --cov-report term-missing",
        shell=True,
    )
    output = grepOut.decode("utf-8")
except subprocess.CalledProcessError as grepexc:
    output = grepexc.output.decode("utf-8")
    test_failed = True
    print("error code", grepexc.returncode, "\n\n --------- \n", output)


save_path = os.path.join("dev", "pytest-coverage")
Path(save_path).mkdir(parents=True, exist_ok=True)

save_path = os.path.join(save_path, "pytest-coverage.txt")

if os.path.exists(save_path):
    os.remove(save_path)
with open(save_path, "w") as f:
    f.write(output)


if test_failed is True:
    raise ValueError("Tests did not pass")