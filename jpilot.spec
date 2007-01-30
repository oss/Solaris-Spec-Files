Summary: jpilot
Name: jpilot
Version: 0.99.9
Release: 1
Copyright: GPL
Group: Applications/Productivity
Source: %{name}-%{version}.tar.gz
URL: http://http://www.jpilot.org/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: gtk2-devel
Requires: pilot-link gtk2
BuildRequires: pilot-link

%description
Graphical interface to palm pilots.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc" CXX="g++"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX

./configure --disable-gtk2 --prefix=/usr/local --enable-prometheon

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
#mv $RPM_BUILD_ROOT/usr/local/lib/charset.alias $RPM_BUILD_ROOT/usr/local/lib/charset.alias.jpilot

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /usr/local/lib/charset.alias ] ; then
    echo pointing /usr/local/lib/charset.alias to /usr/local/lib/charset.alias.jpilot
   ln -s /usr/local/lib/charset.alias.jpilot /usr/local/lib/charset.alias
fi
    

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/lib/jpilot/plugins/*.so*
/usr/local/man/man1/*
/usr/local/share/*

