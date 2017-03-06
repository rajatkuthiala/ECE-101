
------------------------------------------------------
Easy Python Decompiler is a python bytecode decompiler.
No python installation is needed for decompiling!
------------------------------------------------------

Bytecode from python version 1.0 to 3.3 are supported.
You can either decompile a single file or a whole directory. 
Recursing into sub-directories is not yet supported.

There are are two engines which performs the actual decompilation.

- The Uncompyle2 engine is python based 
      (i.e. it runs on an embedded python interpreter).
  It can decompile only python 2.5, 2.6 & 2.7. 
  Unicode file names are not supported by this engine. 

- The Decompyle++ engine is a native engine. 
  It can decompile all python versions upto 3.3.
  It is faster than Uncompyle2 but it is error prone
  and may crash on certain files.
  Unicode file names are supported by this engine.

Using automatic selects the best engine for decompiling
a particular file. It uses Uncompyle2 for 
python 2.5, 2.6 & 2.7 and Decompyle++ for other versions.
This is used as the default engine.

The decompiled file has an extension of 
.pyc_dis or .pyo_dis as the case may be.

Note : If you run this on Windows XP, you may experience 
strange visual artifacts but decompiling functionality will not be affected.

Please report to the following link if you find any bugs
https://forum.tuts4you.com/topic/34427-python-bytecode-decompiler/