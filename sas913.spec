Summary: SAS System
Name: sas
Version: 9.1.3
Release: 1
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /usr/local/src/%{name}-root

%description
SAS System: The Power to Know
%prep
%setup -q -c -n %{name}-%{version}

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -r * %{buildroot}

%post
cat <<EOF
This version has no license. You will need to obtain and install a license.

You may wish to:
    ln -s /usr/local/SAS/SAS_9.1/sas /usr/local/bin/sas 

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/SAS

