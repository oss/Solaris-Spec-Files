Summary: Daily ADS Summary 
Name: ads-sum
Version: 1.0.1
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: ads-sum-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: php-common php-devel

%description
This is a php script that looks in a specified mailfolder, usually 
.AUTO-DELETED-SPAM, and generates a summary of the lowest 20 scoring 
messages from the past 24 hours. The output should be redirected to
a file in the user's Maildir.

%prep
%setup -q 

%install
mkdir -p %{buildroot}/usr/local/bin
cp ads-sum %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(755, root, bin)
%doc
/usr/local/bin/ads-sum

%changelog
* Mon Jan 5 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.01-1
- added starttime and endtime filtering
- added tiebreaker mode
- added command line options

* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-2
- changed permissions to 755 

* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-1
- bumped to next version

* Thu Apr 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.91-1
- bumped to next version

* Wed Apr 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.87-1
- first release

