Summary: Locked file lister
Name: lslk
Version: 1.29
Release: 1ru
Group: System Environment/Base
License: BSD type
Source: lslk_1.29.tar
BuildRoot: /var/tmp/%{name}-root


%description
Locked files lister

%prep
%setup -n lslk_1.29

%build
./Configure -n solariscc
make

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
install lslk $RPM_BUILD_ROOT/usr/local/bin
install lslk.8 $RPM_BUILD_ROOT/usr/local/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat<<EOF
SECURITY NOTICE: lslk is setgid sys
EOF

%files
%defattr(-,bin,bin)
%doc README
%attr(2755,root,sys) /usr/local/bin/lslk
%attr(0444,-,-)/usr/local/man/man8/lslk.8
