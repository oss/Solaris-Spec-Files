%define name drupal
%define version 5.5
%define release 1
%define prefix /usr/local
%define drupaldir %{_datadir}/drupal

Summary:        An open source content management system.
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Group:          Applications/Internet
Source:         %{name}-%{version}.tar.gz
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
%setup -q

%build
find . -type d -exec chmod g-s {} \;

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -d %{buildroot}%{drupaldir}
cp -pr * %{buildroot}%{drupaldir}

%post
cat << EOF
This RPM just installs drupal, you still must configure it.
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
* Wed Dec 12 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.5-1
- Bumped to 5.5.
* Thu Nov 8 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.3-1
- Initial build.
