Name:       	bspwm
Version:    	0.9.10
Release:    	1%{?dist}
Summary:    	A tiling window manager based on binary space partitioning.

License:    	BSD

URL:        	https://github.com/baskerville/bspwm
Source0:    	%{URL}/archive/refs/tags/%{version}.tar.gz

BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-xinerama)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(xcb-ewmh)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-randr)

%description
bspwm is a tiling window manager that represents windows as the leaves of a full binary tree.

It only responds to X events, and the messages it receives on a dedicated socket.

%global debug_package %{nil}

%prep
%autosetup

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p %{buildroot}/usr/share/xsessions
mv %{buildroot}/usr/local/share/xsessions/bspwm.desktop %{buildroot}/usr/share/xsessions/bspwm.desktop

%files
%license LICENSE
%doc README.md doc/CHANGELOG.md doc/CONTRIBUTING.md doc/INSTALL.md doc/MISC.md doc/TODO.md
%dir /usr/local/share/doc/bspwm
%dir /usr/local/share/doc/bspwm/examples
/usr/local/bin/bspwm
/usr/local/bin/bspc
/usr/local/share/man/man1/bspwm.1
/usr/local/share/man/man1/bspc.1
/usr/local/share/bash-completion/completions/bspc
/usr/local/share/fish/vendor_completions.d/bspc.fish
/usr/local/share/zsh/site-functions/_bspc
/usr/share/xsessions/bspwm.desktop
/usr/local/share/doc/bspwm/**/*
/usr/local/share/doc/bspwm/CHANGELOG.md
/usr/local/share/doc/bspwm/CONTRIBUTING.md
/usr/local/share/doc/bspwm/INSTALL.md
/usr/local/share/doc/bspwm/MISC.md
/usr/local/share/doc/bspwm/README.md
/usr/local/share/doc/bspwm/TODO.md


%changelog
* Sun Jun 20 2021 Hayden Young <hi@hbjy.dev>
- Create initial bspwm package.

