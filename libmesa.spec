Name: libmesa
Version: 6.4.2
Release: 1
Copyright: MIT
Group: System Environment/Libraries
Summary: 3D Graphics Library
Source0: MesaLib-%{version}.tar.bz2
Source1: MesaGLUT-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root

%description
Mesa is a 3-D graphics library with an API which is very similar to that 
of OpenGL.* To the extent that Mesa utilizes the OpenGL command syntax 
or state machine, it is being used with authorization from Silicon 
Graphics, Inc.(SGI). However, the author does not possess an OpenGL 
license from SGI, and makes no claim that Mesa is in any way a 
compatible replacement for OpenGL or associated with SGI. Those who want 
a licensed implementation of OpenGL should contact a licensed vendor. 

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version} 

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use {%name}.

%prep
%setup -q -n Mesa-%{version}
cd ..
bzip2 -dc $RPM_SOURCE_DIR/MesaGLUT-%{version}.tar.bz2 | tar xf -
cd Mesa-%{version}

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

make sunos5

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local 
make install DESTDIR=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/local/lib/*so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 6.4.2-1
- Initial Rutgers release
