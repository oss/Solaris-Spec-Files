Summary: NCDware
Name: NCDware
Version: 1.0
Release: 1
Copyright: Commercial
Group: Misc
Source: NCDware.tar.bz2
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root

%description
(null)
%prep
%setup -q -n NCDware

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/
cp -r * $RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/



