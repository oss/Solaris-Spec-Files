Summary: Mail_mimeDecode provides classes to decode mime messages
Name: pear-Mail_mimeDecode
Version: 1.5.0
Release: 3
License: BSD 
Group: Development/Libraries
Source: Mail_mimeDecode-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-Mail_Mime

%description
Provides a class to deal with the decoding and interpreting of mime messages.
This package used to be part of the Mail_Mime package, but has been split off.

%prep
%setup -q -n Mail_mimeDecode-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Mail
mkdir -p %{buildroot}/usr/local/lib/php/test/Mail

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp *.php %{buildroot}/usr/local/lib/php/Mail
cp -r tests/ %{buildroot}/usr/local/lib/php/test/Mail

%files
%defattr(-,root,bin)
%doc
/usr/local/lib/php/Mail/mimeDecode.php
/usr/local/lib/php/test/Mail/tests/*

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5.0-1
- Fixed php requires.
