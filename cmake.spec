Summary: A cross-platform, open-source build system
Name: cmake
Version: 2.6.0
Release: 1
Group: Development/Tools
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
License: BSD
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: make 

%description
CMake is a family of tools designed to build, test and package software. CMake is used to control 
the software compilation process using simple platform and compiler independent configuration files. 
CMake generates native makefiles and workspaces that can be used in the compiler environment of your 
choice. CMake is quite sophisticated: it is possible to support complex environments requiring system 
introspection, pre-processor generation, code generation and template instantiation. In addition to 
controling the build process, CMake includes CTest for testing and CPack for packaging.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./bootstrap --prefix=/usr/local
gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/cmake-2.6
%{_bindir}/*
%{_datadir}/cmake-2.6
%{_mandir}/man1/*

%changelog
* Tue Jul 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.6.0-1
- Initial build.
