Summary: DocBook StyleSheets
Name:      docbook
Version:   4.2
Release:   4
Source:   %{name}-%{version}.tar.gz
Group: Networking/Utilities
License: Kinda BSDish
BuildRoot: %{_tmppath}/rpm-%{name}-root
Prefix: /usr/local

%description
DocBook.

%prep
%setup 
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/xml/docbook

%setup


%build

%install
#rm %{name}-%{version}/ChangeLog %{name}-%{version}/README
rm README ChangeLog *.zip
cp -a  * $RPM_BUILD_ROOT/usr/local/share/xml/docbook

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
/usr/local/*





