%define python_version 2.4
%define python_sitearch %{_libdir}/python%{python_version}/site-packages

Summary:	Debian's Advanced Packaging Tool with RPM support
Name:		apt
Version:	0.5.15lorg3.95
Release:	2.git20090203
Group:		System Environment/Base
URL:		http://apt-rpm.org/
License:	GPLv2+ 
Source0:	%{name}-%{version}.tar.gz
Source1:	default.conf
Source2:	sources.list
Source3:	rpmpriorities
Patch0:		apt-0.5.15lorg3.x-cache-corruption.patch
Patch1:		apt-0.5.15lorg3.9x-paths.patch
Patch2:         apt-0.5.15lorg3.9x-sunlibc.patch
Patch3:         apt-0.5.15lorg3.9x-manpagefix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	python >= 2.4, libxml2-devel >= 2.6, sqlite-devel, lua-devel
BuildRequires:	rpm-devel, beecrypt-devel >= 4.1.3, zlib-devel, bzip2-devel
BuildRequires:	perl, readline5-devel, ncurses-devel, gawk, pkgconfig
Requires:	gnupg bzip2

Obsoletes:	apt-server-tools
Provides:	apt-server-tools

%description
APT-RPM is a port of Debian's apt tools for RPM based distributions.
It provides the apt-get utility that provides a simple, safe way to
install and upgrade packages. APT features complete installation
ordering, multiple source capability and several other useful
features.

%package devel
Summary: Development files and documentation for APT's libapt-pkg
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: rpm-devel pkgconfig

%description devel
This package contains development files for developing with APT's
libapt-pkg package manipulation library, modified for RPM.

%package python
Summary: Python bindings for libapt-pkg
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description python
The apt-python package contains a module which allows python programs
to access the APT library interface.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

# fix docs to reference correct paths
perl -pi -e \
 's|\bconfigure-index\.gz\b|configure-index| ;
  s|/usr/share/doc/apt/|%{_docdir}/%{name}-%{version}/|' \
 doc/apt.ent doc/offline.sgml

# don't require python, lua etc because of stuff in doc/contrib
find contrib/ -type f | xargs chmod 0644

%build
PATH="/opt/SUNWspro/bin:${PATH}" 
CC="gcc" CXX="g++" 
CPPFLAGS="-I/usr/local/include -I/usr/local/include/rpm" 
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
LD_OPTIONS="-L/usr/local/lib -R/usr/local/lib -lrpmdb -lbeecrypt"
export PATH CC CXX CPPFLAGS LD LDFLAGS LD_OPTIONS

./configure \
        --prefix=%{_prefix}             \
        --exec-prefix=%{_exec_prefix}   \
        --sysconfdir=%{_sysconfdir}     \
        --localstatedir=%{_var}         \
        --mandir=%{_mandir}             \
        --disable-dependency-tracking   \
        --disable-static                \
        --disable-nls

gmake

gmake -C python PYTHON="/usr/local/bin/python"
python -O -c "import py_compile; py_compile.compile('python/apt.py')"

%install
rm -rf %{buildroot}

PATH=/usr/local/gnu/bin:${PATH}
export PATH

gmake install DESTDIR=%{buildroot} includedir=%{_includedir}/apt-pkg

# The state files
mkdir -p %{buildroot}%{_var}/cache/apt/archives/partial
mkdir -p %{buildroot}%{_var}/cache/apt/genpkglist
mkdir -p %{buildroot}%{_var}/cache/apt/gensrclist
mkdir -p %{buildroot}%{_var}/state/apt/lists/partial

# The config files
mkdir -p %{buildroot}%{_sysconfdir}/apt
mkdir -p %{buildroot}%{_sysconfdir}/apt/sources.list.d
mkdir -p %{buildroot}%{_sysconfdir}/apt/vendors.list.d
install -pm 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/apt/apt.conf.d/default.conf
install -pm 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/apt/sources.list
install -pm 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/apt/

# GPG keys
mkdir -p %{buildroot}%{_sysconfdir}/apt/gpg/

# The python bindings
mkdir -p %{buildroot}%{python_sitearch}/
install -pm 755 python/_apt.so %{buildroot}%{python_sitearch}/
install -pm 644 python/apt.py* %{buildroot}%{python_sitearch}/
touch %{buildroot}%{python_sitearch}/apt.pyo

# Nightly updater scripts & default config
install -Dpm 755 contrib/apt-cron/apt.init %{buildroot}/%{_sysconfdir}/apt/
install -Dpm 755 contrib/apt-cron/apt.cron %{buildroot}/%{_sysconfdir}/apt/
install -Dpm 644 contrib/apt-cron/apt.sysconfig %{buildroot}/%{_sysconfdir}/apt/

# GPG checker from contrib
install -pm 755 contrib/gpg-check/*.lua %{buildroot}/%{_datadir}/apt/scripts

# nuke .la files
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS* COPYING* ABOUT* TODO doc/examples/ contrib/

%dir %{_sysconfdir}/apt/
%config(noreplace) %{_sysconfdir}/apt/rpmpriorities
%config(noreplace) %{_sysconfdir}/apt/sources.list
%dir %{_sysconfdir}/apt/apt.conf.d/
%config %{_sysconfdir}/apt/apt.conf.d/default.conf
%config %{_sysconfdir}/apt/apt.conf.d/multilib.conf
%dir %{_sysconfdir}/apt/sources.list.d/
%dir %{_sysconfdir}/apt/vendors.list.d/
%config(noreplace) %{_sysconfdir}/apt/apt.sysconfig
%{_sysconfdir}/apt/apt.init
%{_sysconfdir}/apt/apt.cron
%{_sysconfdir}/apt/gpg
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-shell
%{_bindir}/apt-get
%{_bindir}/countpkglist
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_bindir}/genbasedir
%{_libdir}/libapt-pkg*.so.*
%dir %{_libdir}/apt/
%{_libdir}/apt/methods
%dir %{_datadir}/apt
%dir %{_datadir}/apt/scripts
%{_datadir}/apt/scripts/gpg-check.lua
%{_datadir}/apt/scripts/gpg-import.lua
%{_var}/cache/apt
%{_var}/state/apt
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/apt-pkg
%{_libdir}/libapt-pkg*.so
%{_libdir}/pkgconfig/libapt-pkg.pc

%files python
%defattr(-,root,root,-)
%{python_sitearch}/_apt.so
%{python_sitearch}/apt.py*

%changelog
* Fri May 08 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.5.15lorg3.95-2.git20090203
- Added Obsoletes:/Provides: apt-server-tools
* Wed Feb 18 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.5.15lorg3.95-1.git20090203
- Latest git snapshot of apt-rpm 
- Built for usage with rpm-4.4.2.3
- Configured (default.conf) to use the external RPM binary rather than librpm
  (spec file scriptlets fail otherwise)
