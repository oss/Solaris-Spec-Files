Summary: Maple 8.0
Name: maple8
Version: 8.01
Release: 1
Copyright: Commercial
Group: Misc
Source: maple-8.01.tar
Distribution: Rutgers Internal ONLY
BuildRoot: %{_tmppath}/%{name}-root
BuildArch     : noarch

%description
(null)
%prep
%setup -q -n usr

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/
cp -r * $RPM_BUILD_ROOT/usr/
cd $RPM_BUILD_ROOT/usr/local
ln -s maple-8.01 maple

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/maple-8.01
%config(noreplace) /usr/local/maple


