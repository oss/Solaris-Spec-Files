%define name webtools_weeblefm
%define version 0.3
%define release 3
%define prefix /usr/local

Summary: Web file manager 
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
Patch0:  webtools_weeblefm.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4

%description
Web file manager

%prep
%setup -n %{name}-%{version}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/TEXT
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/images
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/PDF
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/images
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/themes
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/tools


install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/docs/*.html $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/docs/TEXT/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/TEXT
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/docs/images/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/images
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/docs/PDF/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/docs/PDF
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/*.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/images/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/images
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/themes/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/themes
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/tools/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/tools


%post
echo "README and README-webtools is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}";
echo "READ the README-webtools!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/html

%defattr(-, root, www)
%doc README LICENSE README-webtools
%{prefix}/%{name}-%{version}/html/*
