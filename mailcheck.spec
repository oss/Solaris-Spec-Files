Summary: Mail monitoring tool
Name: mailcheck
Version: 3.0
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: mailcheck-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: time

%description
This is a script to monitor mail usage and gather system impact info.
We usually run it via cron every 15 minutes and once a day with the -t
flag to insert headers into the logs. We run it mainly on our
pop/imap and /var/mail nfs server to keep an eye on the system
load and user use of pop/imap connections. 

cron example:
  0          0,12 * * * /usr/local/sbin/mailcheck -t
  0,15,30,45 *    * * * /usr/local/sbin/mailcheck -s -m /purgatory/mail

NOTE: the script uses gnu-time

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}

echo "%defattr(-, root, bin)" >RPM_FILE_LIST
find . -type f -print | grep -v RPM_FILE_LIST | sed 's/^\.//' >>RPM_FILE_LIST

%clean
rm -rf %{buildroot}

%files -f RPM_FILE_LIST

%changelog
* Thu Feb 21 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 3.0-1
- updated to version 3.0 provided by Basil
