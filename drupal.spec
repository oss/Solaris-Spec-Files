%define name drupal
%define version 6.0beta2
%define realversion 6.0-beta2
%define release 1
%define prefix /usr/local
%define drupaldir %{_datadir}/drupal

Summary:        An open source content management system.
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Group:          Applications/Internet
Source:         %{name}-%{realversion}.tar.gz
URL:            http://www.drupal.org
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot:      %{_tmppath}/%{name}-root
Requires:       php >= 4.3.3, mysql

%description
Drupal is a free software package that allows an individual or a community of users to easily publish, 
manage and organize a wide variety of content on a website. Drupal is ready to go from the moment you download it. 
It even has an easy-to-use web installer! Drupal is open-source software distributed under the GPL 
("General Public License") and is maintained and developed by a community of thousands of users and developers. 
Drupal is free to download and use.

%prep
%setup -q -n %{name}-%{realversion}

%build
find . -type d -exec chmod g-s {} \;

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -d %{buildroot}%{drupaldir}
cp -pr * %{buildroot}%{drupaldir}

%post
cat << EOF
You need to configure xxx by doing yyy.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt INSTALL* LICENSE* MAINTAINERS.txt UPGRADE.txt drupal-README.fedora sites/all/README.txt
%{drupaldir}
%exclude %{drupaldir}/CHANGELOG.txt
%exclude %{drupaldir}/INSTALL*
%exclude %{drupaldir}/LICENSE*
%exclude %{drupaldir}/MAINTAINERS.txt
%exclude %{drupaldir}/UPGRADE.txt

%changelog
* Tue Oct 30 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 6.0-beta2
- Initial build.
