from __future__ import annotations

from importlib.metadata import version

import ortools
import pytest

from common.data_loader import load_people_q1, load_people_q2, load_people_q3
from common.grouping import group_q1, group_q2, group_q3


def main() -> None:
    q1 = load_people_q1()
    q2 = load_people_q2()
    q3 = load_people_q3()
    import sys

    print(f"executable={sys.executable}")
    print(f"python={sys.version.split()[0]}")
    print(f"ortools={ortools.__version__}")
    print(f"pytest={pytest.__version__}")
    print(f"ruff={version('ruff')}")
    print(f"q1_persons={len(q1)} q1_groups={len(group_q1(q1))}")
    print(f"q2_persons={len(q2)} q2_groups={len(group_q2(q2))}")
    print(f"q3_persons={len(q3)} q3_groups={len(group_q3(q3))}")


if __name__ == "__main__":
    main()
