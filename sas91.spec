%define __find_requires %{nil}
%define __find_provides %{nil}

Summary: SAS System
Name: sas
Version: 9.1
Release: 1
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
SAS System: The Power to Know
%prep
%setup -q -n SAS_9.1

%build
# Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/SAS_9.1
cp -r * $RPM_BUILD_ROOT/usr/local/SAS_9.1

%post
cat <<EOF
This version has an expired license. You will need to obtain and install
a new license.

You may wish to:
    ln -s /usr/local/SAS_9.1/sas /usr/local/bin/sas 

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/SAS_9.1

