Name: atk
Version: 1.10.3
Release: 2
Copyright: LGPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
Summary: Interfaces for accessibility support.
BuildRoot: %{_tmppath}/%{name}-root
Requires: glib2 >= 2.8.6
BuildRequires: glib2-devel >= 2.8.6

%description
The ATK library provides a set of interfaces for adding
accessibility support to applications and graphical user
interface toolkits. By aupporting the ATK interface, an
application or toolkit can be used with tools such as
screen readers, magnifiers, and alternative input devices.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version}
BuildRequires: glib2-devel >= 2.8.6
Group: Development
%description devel
The atk-devel package includes the header files and
developer docs for the atk package.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n %{name}-%{version}

%build
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc"
#PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
#export LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS


# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-gtk-doc

# When I attempted to compile with cc I was receiveing the following:
#Making all in docs
#make: Fatal error: Don't know how to make target `all-local'
#Current working directory /usr/local/src/rpm-packages/BUILD/atk-1.9.0/docs
#*** Error code 1
#make: Fatal error: Command failed for target `all-recursive'
#Current working directory /usr/local/src/rpm-packages/BUILD/atk-1.9.0
#*** Error code 1
#make: Fatal error: Command failed for target `all'
# so I switched to gmake
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*so
/usr/local/lib/*so*
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
* Tue Feb 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.9.0-5
- Fixed library linking problem
* Tue Feb 21 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.9.0-5
- Built on top of latest version of glib2
* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-4
- switched back to gcc; see glib2.spec for reason

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-3
- changed gcc to cc

* Wed May 25 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-2
- Made a few tweaks to the spec file

* Tue May 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-1
- Upgraded to latest release
