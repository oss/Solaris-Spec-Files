%define name webtools_imapcp
%define version 0.3
%define release 6
%define prefix /usr/local

Summary: Web application addon for converting mail folders
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4

%description
Web application addon for converting mail folders   

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin

install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/mvfolder $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/rimap $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0551 $RPM_BUILD_DIR/%{name}-%{version}/src/convert.pl $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0755 $RPM_BUILD_DIR/%{name}-%{version}/src/imapd $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/

%post
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "This package uses a version of imapd from the imap package (imap-2002.RC6-RU3), if you use NFS you will also want mlock installed.";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}";
echo "READ the README!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/html
%dir %{prefix}/%{name}-%{version}/webbin

%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
%{prefix}/%{name}-%{version}/webbin/*
