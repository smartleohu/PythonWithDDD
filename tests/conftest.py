import sys
from pathlib import Path

TEST_DIR = Path(__file__)
ROOT_DIR = TEST_DIR.parents[1]

sys.path.append(str(ROOT_DIR))
