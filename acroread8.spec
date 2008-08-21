Name:		acroread8
Version:	8.1.2SU1
License:	Commercial
Group:		Applications/PDF
Summary:	Acrobat Reader 8
Release:	1
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		AdobeReader_enu-8.1.2_SU1-1.sparc.tar.gz
Requires:	vpkg-SUNWgnome-libs
BuildRequires:	sed
BuildRoot:	%{_tmppath}/%{name}-root

%description
Acrobat Reader is Adobe's PDF reading software.

%prep
%setup -q -n AdobeReader

%build
# Nothing to build

%install
rm -rf %{buildroot}

./INSTALL --install_path=%{buildroot}/opt

sed 's!\(LD_LIBRARY_PATH=\"`prepend \"\)!\1/usr/local/lib:!' \
	-i %{buildroot}/opt/Adobe/Reader8/bin/acroread

rm -rf %{buildroot}/opt/Adobe/HelpViewer

mv "%{buildroot}/opt/Adobe/Help/en_US/Adobe Reader/8.0" \
	%{buildroot}/opt/Adobe/Reader8/Help

%clean
rm -rf %{buildroot}

%post
cat << EOF
======================================================
Be sure to add /opt/Adobe/Reader8/bin to your PATH.
======================================================

EOF

%files
%defattr(-, root, bin)
%docdir /opt/Adobe/Reader8/Help
/opt/Adobe/Reader8

%changelog
* Thu Aug 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 8.1.2SU1-1
- Updated to version 8.1.2SU1
