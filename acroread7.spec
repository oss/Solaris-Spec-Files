Name: acroread7
Version: 7.0
Copyright: Commercial
Group: Applications/PDF
Summary: Acrobat Reader 7
Release: 1
Packager: Rutgers University
Source: acrobat7-inst.tar.gz
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
cp -R Acrobat7 $RPM_BUILD_ROOT/opt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/opt/Acrobat7
