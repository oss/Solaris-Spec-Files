Summary: X image viewer
Name: xv
Version: 3.10a
Release: 2
License: Free for noncommercial use
Group: Amusemnts/Graphics
Source: xv-3.10a.tar.gz
Patch: xv.patch
BuildRoot: /var/tmp/%{name}-root
Requires: gs gzip

%description
Xv is a popular image viewer for X11.  It is free for noncommercial
use only.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/bin
for i in xv bggen vdcomp xcmap xvpictoppm ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin/$i
done
install -m 0644 docs/xvp2p.man $RPM_BUILD_ROOT/usr/local/man/man1/xvpictoppm.1
for i in xv bggen xcmap vdcomp ; do
    install -m 0644 docs/$i.man $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc docs/xvdocs.ps* BUGS CHANGELOG INSTALL README IDEAS
/usr/local/bin/*
/usr/local/man/man1/*