# bspwm.rpm

An RPM spec to install the sensational binary partitioning tiling window
manager, [bspwm](https://github.com/baskerville/bspwm)

## Installation

Install my RPM repository into your system using the latest `hbjy-release`
package on [my RPM server](https://rpm.hbjy.io/el/8/x86_64/).

Then, you should be able to just run `dnf install bspwm`!

## Building

To build, you will need two packages on a Fedora or Rocky Linux machine:

- `mock`
- `rpmdevtools`

Once you have cloned the repository into your rpmbuild/ directory, you can
perform the steps required to build the package.

```shell
# build srpm and rpm
$ make
```

With this command, your SRPM and RPM outputs should be in `srpm/` and `dist/`
respectively.

## See Also

<!-- - [sxhkd.rpm](https://github.com/hbjydev/sxhkd.rpm) - my sxhkd RPM spec -->
