Name: atk
Version: 1.9.0
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
Summary: Interfaces for accessibility support.
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: glib2-devel >= 2.6.4-1

%description
The ATK library provides a set of interfaces for adding accessibility support to applications and graphical user interface toolkits. By aupporting the ATK interface, an application or toolkit can be used with tools such as screen readers, magnifiers, and alternative input devices.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version} glib2-devel >= 2.6.4-1
Group: Development
%description devel
The atk-devel package includes the header files and developer docs for the atk package.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation


%prep
%setup -q -n %{name}-%{version}

%build
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"
CC="gcc"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

./configure --prefix=/usr/local --disable-nls --disable-rebuilds

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/libatk-1.0.so.0
/usr/local/lib/libatk-1.0.so.0.900.0
/usr/local/share/locale/*

%files devel
%defattr(-,root,other)
/usr/local/include/atk-1.0/*
/usr/local/lib/libatk-1.0.so
/usr/local/lib/pkgconfig/atk.pc

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/*

%changelog
* Tue May 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-1
- Upgraded to latest release
