Summary: Daily ADS Summary 
Name: ads-sum
Version: 0.92
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: ads-sum-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: php-common php-devel

%description
This is a php script that looks in a specified mailfolder, usually 
.AUTO-DELETED-SPAM, and generates a summary of the top ten lowest scoring 
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
/usr/local/bin/ads-sum

%changelog
* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-2
- changed permissions to 755 
* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-1
- bumped to next version
* Thu Apr 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.91-1
- bumped to next version
* Wed Apr 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.87-1
- first release
