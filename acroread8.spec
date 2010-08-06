Name:		acroread8
Version:	8.1.7
License:	Commercial
Group:		Applications/PDF
Summary:	Acrobat Reader 8
Release:	1
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Source:		http://ardownload.adobe.com/pub/adobe/reader/unix/8.x/%{version}/enu/AdobeReader_enu-%{version}-1.sparc.tar.bz2
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
* Thu Aug 05 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 8.1.7-1
- Update to 8.1.7

* Wed Sep 30 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 8.1.6-1
- updated to 8.1.6

* Tue Apr 7 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 8.1.4-1
- updated to 8.1.4

* Thu Aug 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 8.1.2SU1-1
- Updated to version 8.1.2SU1
