
Summary: RT, Request Tracker, is an enterprise-grade issue tracking system

Name: RT
Version: 3.0.4
# RT does not come in the standard rt-3.0.4 but rather
# in the ugly form: rt-3-0-4
%define ugly_version 3-0-4
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: rt-%{ugly_version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: apache
Requires: mysql
Requires: apache-module-mod_perl
Requires: perl-module-RT-modules

%description
RT is an enterprise-grade issue tracking system. It allows
organizations to keep track of their to-do lists, who is working
on which tasks, what's already been done, and when tasks were
completed. It is available under the terms of version 2 of the GNU
General Public License (GPL), so it doesn't cost anything to set
up and use.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/src 
cd %{buildroot}/usr/local/src
gzip -dc /usr/local/src/rpm-packages/SOURCES/rt-%{ugly_version}.tar.gz | tar -xf -

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
****************** Request Tracker Installation notes ******************

This RPM only provides the RT source. You will need to configure 
it and then install it. RT requires a series of perl modules but 
this RPM already provides them for you. To learn how to completely
install RT read the file:

/usr/local/src/rt-%{ugly_version}/README 

EOF

%files
%defattr(-,bin,bin)
%doc rt-%{ugly_version}/README 
%doc rt-%{ugly_version}/COPYING 
%doc rt-%{ugly_version}/HOWTO 
%doc rt-%{ugly_version}/docs 
%doc rt-%{ugly_version}/Changelog
/usr/local/src/rt-%{ugly_version}
