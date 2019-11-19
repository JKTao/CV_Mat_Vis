# Visualize OpenCV Mat type in gdb

## Introduction

This repositories provides a debugging visualizer utility when working on OpenCV Mat.

## Install

1. Create the file `~/.gdbinit`.
2. Insert the following lines:

```
python
import sys
sys.path.insert(0, THE_PATH_OF_THIS_REPOSITORY)
import cv_mat_vis.py
cv_mat_vis.register_printers()
end
```

3. Launch gdb or some editor call gdb (like VSCode) then you can print mat as build-in support type variables.

## Warning
1. As a simple utility, it only support small matrix variables with continuous storage, which is adequate for general applications. 
2. The performance overhead is not guaranteed.

## TODO

1. Support Graphical debugger of Clion.
2. Support discontinuous matrix.

## Reference

[python API of GDB](https://www.sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API)



