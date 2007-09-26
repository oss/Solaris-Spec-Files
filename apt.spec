
%define python_sitearch /usr/local/lib/python2.4/site-packages
%define generate_rpmpriorities 0
%define comps %{_datadir}/comps/%{_build_arch}/comps.xml
%define _includedir /usr/local/include
%define _localstatedir /var/local

Summary:	Debian's Advanced Packaging Tool with RPM support
Name:		apt
Version:	0.5.15lorg3.93
Release:	2
Group:		System Environment/Base
URL:		http://apt-rpm.org/
License:	GPLv2+ 
Source0:	http://apt-rpm.org/testing/%{name}-%{version}.tar.bz2
Source1:	apt.conf
Source2:	sources.list
Source3:	vendors.list
Source4:	apt_preferences
Source5:	rpmpriorities
Source19:	comps2prio.xsl
Source51:	upgradevirt.lua
Source150:	default.conf
Patch1:		apt-0.5.15lorg3.x-cache-corruption.patch
Patch2:		apt-3.93-paths.patch
Patch3:		apt-3.93-bugfixes-gcc.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	python >= 2.4, libxml2-devel, sqlite-devel
BuildRequires:	rpm-devel, beecrypt-devel, zlib-devel, bzip2-devel
BuildRequires:	libstdc++-v6-devel, perl, readline5-devel, ncurses-devel, gawk, pkgconfig
Requires:	gnupg bzip2 apt-config
Requires:	bzip2
Requires:	apt-config
BuildArch:	sparc64

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
Requires: rpm-devel
Requires: pkgconfig

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
%patch1 -p0 -b .mmap
%patch2 -p1

# fix docs to reference correct paths
perl -pi -e \
 's|\bconfigure-index\.gz\b|configure-index| ;
  s|/usr/share/doc/apt/|%{_docdir}/%{name}-%{version}/|' \
 doc/apt.ent doc/*/apt.ent.* doc/offline.sgml contrib/apt-wrapper/apt.ent

/usr/local/gnu/bin/install -pm 644 %{SOURCE19} comps2prio.xsl

# don't require python, lua etc because of stuff in doc/contrib
find contrib/ -type f | xargs chmod 0644

%patch3 -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="gcc" CXX="g++" CPPFLAGS="-I/usr/local/include -I/usr/local/include/rpm" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LD_OPTIONS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS LD_OPTIONS

./configure \
	--prefix="/usr/local" \
	--exec-prefix="/usr/local" \
	--sysconfdir="/usr/local/etc" \
	--localstatedir="/var/local" \
	--disable-nls

gmake

gmake -C python PYTHON="/usr/local/bin/python"
python -O -c "import py_compile; py_compile.compile('python/apt.py')"

%install
rm -rf %{buildroot}

PATH=/usr/local/gnu/bin:$PATH
export PATH

gmake install DESTDIR=%{buildroot} includedir=%{_includedir}/apt-pkg
%find_lang %{name}

# The state files
mkdir -p %{buildroot}%{_localstatedir}/cache/apt/archives/partial
mkdir -p %{buildroot}%{_localstatedir}/cache/apt/genpkglist
mkdir -p %{buildroot}%{_localstatedir}/cache/apt/gensrclist
mkdir -p %{buildroot}%{_localstatedir}/lib/apt/lists/partial

# The config files
mkdir -p %{buildroot}%{_sysconfdir}/apt
mkdir -p %{buildroot}%{_sysconfdir}/apt/apt.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/apt/sources.list.d
mkdir -p %{buildroot}%{_sysconfdir}/apt/vendors.list.d
install -pm 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/apt/apt.conf
install -pm 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/apt/sources.list
install -pm 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/apt/vendors.list
install -pm 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/apt/preferences
install -pm 644 rpmpriorities %{buildroot}/%{_sysconfdir}/apt/

# install config parts
install -pm 644 %{SOURCE150} %{buildroot}%{_sysconfdir}/apt/apt.conf.d/

# # GPG keys
mkdir -p %{buildroot}%{_sysconfdir}/apt/gpg/

# Lua scripts
mkdir -p %{buildroot}%{_datadir}/apt/scripts
for script in %{SOURCE51} ; do
 install -pm 755 $script %{buildroot}%{_datadir}/apt/scripts
done

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

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS* COPYING* ABOUT* TODO comps2prio.xsl doc/examples/ contrib/
%doc ChangeLog lua/COPYRIGHT

%dir %{_sysconfdir}/apt/
%config(noreplace) %{_sysconfdir}/apt/apt.conf
%config(noreplace) %{_sysconfdir}/apt/preferences
%config(noreplace) %{_sysconfdir}/apt/rpmpriorities
%config(noreplace) %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/apt/vendors.list
%dir %{_sysconfdir}/apt/apt.conf.d/
# NOTE: no noreplace because we WANT to be able to change the defaults
# without user intervention!
%config %{_sysconfdir}/apt/apt.conf.d/default.conf
%config %{_sysconfdir}/apt/apt.conf.d/multilib.conf
%dir %{_sysconfdir}/apt/sources.list.d/
%dir %{_sysconfdir}/apt/vendors.list.d/
%config(noreplace) %{_sysconfdir}/apt/*
%{_sysconfdir}/apt/apt.cron
%{_sysconfdir}/apt/gpg/
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
%{_libdir}/apt/
%dir %{_datadir}/apt/
%dir %{_datadir}/apt/scripts/
%{_datadir}/apt/scripts/gpg-check.lua
%{_datadir}/apt/scripts/gpg-import.lua
%{_datadir}/apt/scripts/upgradevirt.lua
%{_localstatedir}/cache/apt/
%{_localstatedir}/lib/apt/
/usr/local/share/man/man5/*
/usr/local/share/man/man8/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/apt-pkg/
%{_libdir}/libapt-pkg*.so
%{_libdir}/pkgconfig/libapt-pkg.pc
/usr/local/lib/libapt-pkg.a

%files python
%defattr(-,root,root,-)
%{python_sitearch}/_apt.so
%{python_sitearch}/apt.py*

%changelog
* Tue Sep 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.5.15lorg3.93-1
- Inital Rutgers attempt
