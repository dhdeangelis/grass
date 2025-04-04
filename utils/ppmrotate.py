#!/usr/bin/env python3
#
# ppmrotate.py: Rotate PPM images
#
#  AUTHOR: Glynn Clements (Python version)
#          Vaclav Petras (separate script)
#      Earlier Bourne script version by Hamish Bowman,
#      https://grasswiki.osgeo.org/wiki/Talk:Color_tables
#
#   (C) 2009-2017 by the GRASS Development Team
#       This program is free software under the GNU General Public
#       License (>=v2). Read the file COPYING that comes with GRASS
#       for details.
#

import sys
import os
import atexit
import array
from pathlib import Path

import grass.script as gs

tmp_img = None

height = None
width = None


def cleanup():
    if tmp_img:
        gs.try_remove(tmp_img)


# def rotate(src, dst):
#     grass.call(["convert", "-rotate", "90", src, dst])


def read_ppm(src):
    global width, height
    text = Path(src).read_bytes()

    i = 0
    j = text.find("\n", i)
    if text[i:j] != "P6":
        raise OSError(text[i:j] + " != P6. Is the file PPM?")
    i = j + 1
    j = text.find("\n", i)
    w, h = text[i:j].split()
    width = int(w)
    height = int(h)
    i = j + 1
    j = text.find("\n", i)
    maxval = text[i:j]
    if int(maxval) != 255:
        msg = "Max value in image != 255"
        raise OSError(msg)
    i = j + 1
    return array.array("B", text[i:])


def write_ppm(dst, data):
    w = height
    h = width
    with open(dst, "wb") as fh:
        fh.write("P6\n%d %d\n%d\n" % (w, h, 255))
        data.tofile(fh)


def rotate_ppm(srcd):
    dstd = array.array("B", len(srcd) * "\0")
    for y in range(height):
        for x in range(width):
            for c in range(3):
                old_pos = (y * width + x) * 3 + c
                new_pos = (x * height + (height - 1 - y)) * 3 + c
                dstd[new_pos] = srcd[old_pos]
    return dstd


def flip_ppm(srcd):
    dstd = array.array("B", len(srcd) * "\0")
    stride = width * 3
    for y in range(height):
        dy = height - 1 - y
        dstd[dy * stride : (dy + 1) * stride] = srcd[y * stride : (y + 1) * stride]
    return dstd


def ppmtopng(dst, src):
    if gs.find_program("g.ppmtopng", "--help"):
        gs.run_command("g.ppmtopng", input=src, output=dst, quiet=True)
    elif gs.find_program("pnmtopng"):
        with open(dst, "wb") as fh:
            gs.call(["pnmtopng", src], stdout=fh)
    elif gs.find_program("convert"):
        gs.call(["convert", src, dst])
    else:
        gs.fatal(_("Cannot find g.ppmtopng, pnmtopng or convert"))


def convert_and_rotate(src, dst, flip=False):
    global tmp_img

    ppm = read_ppm(src)
    if flip:
        ppm = flip_ppm(ppm)
    ppm = rotate_ppm(ppm)
    to_png = False
    if dst.lower().endswith(".png"):
        to_png = True
    # TODO: clean up the file
    tmp_img = gs.tempfile() + ".ppm" if to_png else dst
    write_ppm(tmp_img, ppm)
    if to_png:
        ppmtopng(dst, tmp_img)


def main():
    os.environ["GRASS_OVERWRITE"] = "1"

    infile = sys.argv[1]
    outfile = sys.argv[2]

    convert_and_rotate(infile, outfile, flip=False)


if __name__ == "__main__":
    atexit.register(cleanup)
    main()
