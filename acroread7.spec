%define __find_requires %{nil}
%define __find_provides %{nil}

Name: acroread7
Version: 7.0.1
Copyright: Commercial
Group: Applications/PDF
Summary: Acrobat Reader 7
Release: 3
Packager: Rutgers University
Source: acrobat7.0.1-inst.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Acrobat Reader is Adobe's PDF reading software.

%prep
%setup -q -n Acrobat7

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/opt
cd ..
cp -R Acrobat7 $RPM_BUILD_ROOT/opt/Acrobat7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/opt/Acrobat7
