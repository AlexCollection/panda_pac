Panda pac generator
===================

build with `python build.py > white.pac`

## Use fabric to build local and remote

First, copy `fabfile.example` to `fabfile.py`;

Then, fill `env.directory` with you local repo directory;

Also replace parameters in `remote` function with you own server infomation.

`fab build` to build in local computer, `fab remote build` to build in your server.
