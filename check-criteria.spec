Summary: Check file criteria
Name: check-criteria
Version: 1.0
Release: 2
Group: Applications/Internet
License: RU
Source: check-criteria-20020528
BuildRoot: /var/tmp/%{name}-root

Requires: perl

%description
Check file criteria

%prep
#%setup -q

%build


%install
mkdir -p %{buildroot}/usr/local/bin/
cp $RPM_SOURCE_DIR/check-criteria-20020528 %{buildroot}/usr/local/bin/check-criteria


%post
#blank

%files
%defattr(0755,root,other) 
/usr/local/bin/check-criteria






