
Summary:		Scripts for RPM server
Name: 			rpm-server-scripts
Version: 		0.20020926
Release:		1ru
Copyright: 		GPL
Group: 			Libraries
Source: 		repository-scripts.tar.bz2
#Patch:			rrdtool-rrdtutorial.pod.patch
Buildroot: 		/var/tmp/rpm-server-scripts-root
Prefix:	 		%{_prefix}

%description
Scripts for rpm server

%prep
%setup -q -n repository-scripts

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp update-apt.pl rebuild-apt $RPM_BUILD_ROOT/usr/local/bin/
chmod 0755 $RPM_BUILD_ROOT/usr/local/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
