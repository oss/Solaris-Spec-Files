Summary: Maple 8.0
Name: maple8
Version: 8.0
Release: 1
Copyright: Commercial
Group: Misc
Source: maple8.tar.bz2
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root

%description
(null)
%prep
%setup -q -n maple8

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/maple8
cp -r * $RPM_BUILD_ROOT/usr/local/maple8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/maple8



