#!/usr/bin/env python
# coding=utf-8

"""
This is an Inkscape extension to make a laser path from path elements.
"""

from pathlib import Path
import sys

import inkex
from inkex.command import inkscape_command
from inkex import units

from logger import logger

class MakeLaserPathExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument(
            "--trail_width",
            type=float,
            default=4.0,
            help="Width to leave between laser path (mm)",
        )
        pars.add_argument(
            "--laser_width",
            type=float,
            default=0.01,
            help="Width of the laser path (mm)",
        )

    def _preprocess(self, node, targets):
        """flatten layers and groups to avoid recursion"""
        if not isinstance(node, inkex.ShapeElement):
            return
        if isinstance(node, inkex.Image):
            return
        if isinstance(node, inkex.Group):
            for child in node:
                self._preprocess(child, targets)
        else:
            if node.is_visible():
                targets.append(node.get("id"))
                # the trail width is in mm so convert to px
                # then add the scale factor to get the px value
                stroke_width = (
                    units.convert_unit(str(self.options.trail_width) + "mm", "px")
                    / self.svg.scale
                )
                node.style["stroke-width"] = str(stroke_width)
                node.style["fill"] = "none"

    def effect(self):
        selected_ids = []
        for node in self.svg.selection:
            self._preprocess(node, selected_ids)
        logger.debug(f"selected_ids: {selected_ids}")
        try:
            result = inkscape_command(
                svg=self.svg,
                select=",".join(selected_ids),
                actions="object-stroke-to-path;",
            )
            self.document = inkex.load_svg(result)
            self.svg = self.document.getroot()
            laser_width = (
                units.convert_unit(str(self.options.laser_width) + "mm", "px")
                / self.svg.scale
            )
            for id in selected_ids:
                mod_elem = self.svg.getElementById(id)
                mod_elem.style["stroke-width"] = str(laser_width)
                mod_elem.style["stroke"] = "black"
                mod_elem.style["fill"] = "none"
        except Exception as e:
            logger.error(f"command not found: {e}")


if __name__ == "__main__":
    MakeLaserPathExtension().run()
