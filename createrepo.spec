Summary:	Creates a common metadata repository
Name:		createrepo
Version:	0.4.10
Release:	2
License:	GPL
Group:		System Environment/Base
Source:		%{name}-%{version}.tar.gz
URL:		http://linux.duke.edu/projects/metadata/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	python >= 2.4, libxml2-python
Requires:	yum-metadata-parser
BuildRequires:	python >= 2.4
BuildArch:	sparc64

%description
This utility will generate a common metadata repository from a directory of rpm
packages.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
PATH=/usr/local/gnu/bin:$PATH
export PATH
gmake DESTDIR=$RPM_BUILD_ROOT prefix=/usr/local install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root,-)
%doc ChangeLog README
/usr/local/bin/createrepo
/usr/local/bin/modifyrepo
/usr/local/share/createrepo/dumpMetadata.py
/usr/local/share/createrepo/genpkgmetadata.py
/usr/local/share/createrepo/modifyrepo.py
/usr/local/share/createrepo/readMetadata.py
/usr/local/share/man/man8/createrepo.8

%changelog
* Thu Sep 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.4.10-1
- Initial build
