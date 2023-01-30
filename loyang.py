#!/bin/env python
"""Module to calculate the worth of a vegetable"""
from collections import namedtuple
from enum import auto
from enum import IntEnum
from enum import StrEnum
from typing import List
from typing import Tuple

import IPython


class Vegetable(StrEnum):
    """Vegetable Enum"""

    WHEAT = auto()
    PUMPKIN = auto()
    TURNIP = auto()
    CABBAGE = auto()
    BEAN = auto()
    LEEK = auto()


class Field(IntEnum):
    """Field yield Enum"""

    one = 6
    two = 5
    three = 4
    four = 3


def main():
    """Main function"""
    w = Vegetable.WHEAT
    p = Vegetable.PUMPKIN
    t = Vegetable.TURNIP
    c = Vegetable.CABBAGE
    b = Vegetable.BEAN
    l = Vegetable.LEEK

    Client = namedtuple("Client", ["vegetables", "coins"])
    Market = namedtuple("MarketStall", ["vegetables", "spaces"])
    Field = namedtuple("Field", ["vegetables", "yield"])

    # fmt: off
    regular_client_list: List[Tuple[str, float]] = [
        Client("WW", 20 / 4), Client("WP", 20 / 4), Client("WC", 22 / 4), Client("PT", 22 / 4),
        Client("PC", 24 / 4), Client("TT", 24 / 4), Client("WL", 26 / 4), Client("PB", 26 / 4),
        Client("TC", 26 / 4), Client("PL", 28 / 4), Client("TB", 28 / 4), Client("CB", 30 / 4),
        Client("CL", 32 / 4), Client("BL", 34 / 4),
    ]

    casual_client_list: List[Tuple[str, float]] = [
        Client("WPT", 7), Client("WWB", 8), Client("WTT", 8), Client("WTB", 9), Client("WPL", 9),
        Client("WCC", 9), Client("PPB", 9), Client("PTC", 9), Client("WCL", 10), Client("PTL", 10),
        Client("PCB", 10), Client("PBL", 11), Client("TCL", 11), Client("CBL", 12),
    ]

    market_stall_list: List[Tuple[str, float]] = [
        Market("WPL", 3), Market("WTB", 3), Market("WTL", 3), Market("WCB", 3), Market("WCL", 3),
        Market("WBL", 4), Market("PTC", 3), Market("PTB", 3), Market("PCB", 3), Market("PCL", 4),
        Market("PBL", 5), Market("TCB", 4), Market("TCL", 5), Market("TBL", 5),
    ]

    field_list: List[Tuple[str, float]] = [
        Field("WPT", 6), Field("WPTC", 5), Field("WPTCB", 4), Field("WPTCBL", 3),
    ]

    # Average of possible yield in the game = Σ yield / n
    vegetable_yield: List[Tuple[str, float]] = [
        ("W", 18 / 4), ("P", 18 / 4), ("T", 18 / 4), ("C", 12 / 3), ("B", 7 / 2), ("L", 3 / 1),
    ]
    # fmt: on

    IPython.embed()
    exit(1)


if __name__ == "__main__":
    main()
