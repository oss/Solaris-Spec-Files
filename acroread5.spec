Name: acroread5
Version: 5.0.10
Copyright: Commercial
Group: Applications/PDF
Summary: Acrobat Reader 5
Release: 1
Packager: Rutgers University
Source: acrobat5-inst.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Acrobat Reader is Adobe's PDF reading software.

%prep
%setup -q -n Acrobat5

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/opt
cd ..
cp -R Acrobat5 $RPM_BUILD_ROOT/opt

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/opt/Acrobat5
