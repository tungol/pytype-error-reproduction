Minimal reproduction of pytype error 

This repo contains a minimal reproduction of the error from 
https://github.com/python/typeshed/pull/12745

Run `. setup.sh` to prepare the environment and then run `./pytype_test.py`.

`pytype_test.py` is a streamlined version of the same script from typeshed. File selection
is hardcoded to demonstrate that the error only occurs when the file with ParamSpec is processed
first.
