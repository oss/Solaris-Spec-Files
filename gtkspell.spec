Summary: gtkspell
Name: gtkspell
Version: 2.0.4
Release: 2
Copyright: GPL
Group: Applications/Spelling
Source: http://gtkspell.sourceforge.net/download/gtkspell-2.0.4.tar.gz
URL: http://gtkspell.sf.net
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: aspell gtk2
BuildRequires: aspell gtk2-devel

%description
GTK Spelling library

%prep
%setup -q

%build
PATH=`echo $PATH | sed "s/\/usr\/sfw\/bin//g"`
export PATH
LD_LIBRARY_PATH="/usr/local/lib" \
LD_RUN_PATH="/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0" \
CPPFLAGS="-I/usr/local/include"  \
CC="gcc" ./configure --prefix=/usr/local --disable-gtk-doc


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/




