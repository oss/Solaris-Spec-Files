Name:           mysql-proxy
Version:        0.6.1
Release:        2%{?dist}
Summary:        A proxy for the MySQL Client/Server protocol

Group:          Applications/Databases
License:        GPLv2
URL:            http://forge.mysql.com/wiki/MySQL_Proxy

# I haven't found a link to a direct download location, only to mirrors
Source0:        http://mysql.he.net/Downloads/MySQL-Proxy/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: lua libevent
BuildRequires:  lua
BuildRequires:  libevent-devel
BuildRequires:  mysql-devel
BuildRequires:  glib2-devel
BuildRequires:  gawk
BuildRequires:  check-devel
BuildRequires:  flex

%description
MySQL Proxy is a simple program that sits between your client and MySQL
server(s) that can monitor, analyze or transform their communication.
Its flexibility allows for unlimited uses, common ones include: load balancing,
failover, query analysis, query filtering and modification and many more.

%prep
%setup -q -n %{name}-%{version}


%build
PATH="/usr/local/gnu/bin:/usr/local/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" \
CC="cc" \
CXX="CC" \
CPPFLAGS="-I/usr/local/include -I/usr/local/mysql-5.0.67/include/mysql " \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lm -ldl" \
LUA_LIBS="-L/usr/local/lib -llua" \
LUA_CFLAGS="-I /usr/local/include" \
export PATH CC CXX CPPFLAGS LDFLAGS LUA_LIBS LUA_CFLAGS
./configure --with-mysql=/usr/local/mysql-5.0.67/bin/mysql_config --with-lua
 
gmake

%install
rm -rf $RPM_BUILD_ROOT 
gmake install DESTDIR=$RPM_BUILD_ROOT SUBDIRS=src
rm  examples/Makefile*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS
%doc examples/
/usr/local/sbin/%{name}


%changelog
* Mon Jan 12 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.6.1-2
- rewrote spec file for solaris 9
- added sun cc

* Mon Jun 30 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.6.1-2
- Rebuild to pick up new libevent

* Sat Feb 09 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.6.1-1
- Sync with upstream

* Thu Jan 24 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.6.0-2
- Rebuild to pick up new libevent

* Sat Dec 08 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> - 0.6.0-1
- Upstream released new version
- Fix license tag
- Add BR for check-devel and flex

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.5.1-3
- BR gawk.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.5.1-2
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.5.1-1
- Upstream released new version
- Included examples
* Sun Jul 01 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 0.5.0-1
- First version
