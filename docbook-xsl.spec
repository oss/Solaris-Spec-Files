Summary: DocBook xsl StyleSheets
Name:      docbook-xsl
Version:   1.61.3
Release:   0
Source:   %{name}-%{version}.tar.gz
Group: Networking/Utilities
License: Kinda BSDish
BuildRoot: %{_tmppath}/rpm-%{name}-root
Prefix: /usr/local

%description
DocBook xsl.

%prep
%setup 
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/xml/docbook/xsl

%setup


%build

%install
#rm %{name}-%{version}/ChangeLog %{name}-%{version}/README
cp -a  * $RPM_BUILD_ROOT/usr/local/share/xml/docbook/xsl

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
/usr/local/*





