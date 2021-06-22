all: srpm build

srpm:
	mock -r epel-8-x86_64 --resultdir=srpm/ --buildsrpm --spec SPECS/bspwm.spec --sources=SOURCES/

build:
	mock -r epel-8-x86_64 --resultdir=dist/ --rebuild srpm/bspwm-*.src.rpm

