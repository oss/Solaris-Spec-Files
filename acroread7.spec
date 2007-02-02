%define __find_requires %{nil}
%define __find_provides %{nil}

Name: acroread7
Version: 7.0.9
Copyright: Commercial
Group: Applications/PDF
Summary: Acrobat Reader 7
Release: 1
Packager: Rutgers University
Source: acrobat-%{version}-inst.tar.gz
Requires: vpkg-SUNWgnome-libs
BuildRoot: /var/tmp/%{name}-root

%description
Acrobat Reader is Adobe's PDF reading software.

Note: This package depends on the GNOME libraries provided by Sun.
      Please be sure that your version on Solaris has these libraries.

%prep
%setup -q -n Adobe

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/opt/Adobe
cp -pR Acrobat7.0 $RPM_BUILD_ROOT/opt/Adobe

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

Be sure to add /opt/Adobe/Acrobat7.0/bin to your PATH.

EOF

%files
%defattr(-,root,bin)
/opt/Adobe/Acrobat7.0
