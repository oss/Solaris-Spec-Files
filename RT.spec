
Summary: RT is an enterprise-grade issue tracking system

Name: RT
Version: 3.0.4
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: rt-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: apache
Requires: mysql
Requires: mod_perl
Requires: perl-module-RT-modules
BuildRequires: apache
BuildRequires: mysql
BuildRequires: mod_perl
BuildRequires: perl-module-RT-modules

%description
RT is an enterprise-grade issue tracking system. It allows
organizations to keep track of their to-do lists, who is working
on which tasks, what's already been done, and when tasks were
completed. It is available under the terms of version 2 of the GNU
General Public License (GPL), so it doesn't cost anything to set
up and use.

%prep

%setup -q -n rt-%{version}

%build
./configure --prefix=/usr/local/rt-%{version} --with-mysql --with-modperl1
/usr/sbin/groupadd rt

%install
rm -rf $RPM_BUILD_ROOT
make install
make initialize-database

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -r /usr/local/apache ]; then
	ln -s /usr/local/rt-%{version} /usr/local/rt
	echo /usr/local/rt now points to /usr/local/rt-%{version}
fi
		
%files
%defattr(-,bin,bin)
%doc README COPYING HOWTO docs Changelog
/usr/local/rt-%{version}
/usr/local/rt

