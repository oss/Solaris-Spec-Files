Summary: Check file criteria
Name: check-criteria
Version: 1.0
Release: 1
Group: Applications/Internet
License: RU
Source: check-criteria
BuildRoot: /var/tmp/%{name}-root

Requires: perl

%description
Check file criteria

%prep
#%setup -q

%build


%install
mkdir -p %{buildroot}/usr/local/bin/
cp $RPM_SOURCE_DIR/check-criteria %{buildroot}/usr/local/bin/


%post
#blank

%files
%defattr(0755,root,other) 
/usr/local/bin/check-criteria






