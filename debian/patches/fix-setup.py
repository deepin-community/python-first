--- a/setup.py
+++ b/setup.py
@@ -1,15 +1,22 @@
 from setuptools import setup
 
 import first
+import sys
 
+if sys.version_info[0] >= 3:
+    long_description = (open('README.rst', encoding='utf-8').read() + '\n\n' +
+                        open('HISTORY.rst', encoding='utf-8').read() + '\n\n' +
+                        open('AUTHORS.rst', encoding='utf-8').read())
+else:
+    long_description = (open('README.rst').read() + '\n\n' +
+                        open('HISTORY.rst').read() + '\n\n' +
+                        open('AUTHORS.rst').read())
 
 setup(
     name='first',
     version=first.__version__,
     description='Return the first true value of an iterable.',
-    long_description=(open('README.rst').read() + '\n\n' +
-                      open('HISTORY.rst').read() + '\n\n' +
-                      open('AUTHORS.rst').read()),
+    long_description=long_description,
     url='http://github.com/hynek/first/',
     license=first.__license__,
     author=first.__author__,
