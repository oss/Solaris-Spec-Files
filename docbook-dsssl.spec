Summary: DocBook dssl StyleSheets
Name:      docbook-dsssl
Version:   1.78
Release:   4
Source:   %{name}-%{version}.tar.gz
Group: Networking/Utilities
License: Kinda BSDish
BuildRoot: %{_tmppath}/rpm-%{name}-root
Prefix: /usr/local

%description
DocBook dssl.

%prep
%setup 
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/xml/docbook/dsssl

%setup


%build

%install
#rm %{name}-%{version}/ChangeLog %{name}-%{version}/README
cp -a  * $RPM_BUILD_ROOT/usr/local/share/xml/docbook/dsssl

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
/usr/local/*





