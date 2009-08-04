Summary: Mail_Mime provides classes to create mime messages
Name: pear-Mail_Mime
Version: 1.5.2
Release: 3 
License: BSD
Group: Development/Libraries
Source: Mail_Mime-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: pear-Mail_mimeDecode

%description
Mail_Mime provides classes to deal with the creation and manipulation of mime 
messages.  It allows people to create Email messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

Starting with version 1.4.0, it also allows non US-ASCII chars in filenames, 
subjects, recipients, etc, etc.

%prep
%setup -q -n Mail_Mime-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Mail
mkdir -p %{buildroot}/usr/local/lib/php/test/Mail

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp *.php *.dtd *.xsl %{buildroot}/usr/local/lib/php/Mail
cp -r scripts/ %{buildroot}/usr/local/lib/php/Mail
cp -r tests/ %{buildroot}/usr/local/lib/php/test/Mail

%files
%defattr(-,root,bin)
%doc
/usr/local/lib/php/Mail/mime.php
/usr/local/lib/php/Mail/mimePart.php
/usr/local/lib/php/Mail/xmail.dtd
/usr/local/lib/php/Mail/xmail.xsl
/usr/local/lib/php/test/Mail/tests/*
/usr/local/lib/php/Mail/scripts/phail.php

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5.2-1
- Fixed php requires.
