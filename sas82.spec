Summary: SAS statistical package
Name: sas
Version: 8.2
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
The Power to Know
%prep
%setup -q -n SAS_8.2

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/
cd ..
mv SAS_8.2 $RPM_BUILD_ROOT/usr/local/

#this is so clean works
mkdir SAS_8.2

%post
cat <<EOF
This version will EXPIRE on June 30, 2002.

You may wish to:
    ln -s /usr/local/SAS_8.2/sas /usr/local/bin/sas 

Additional Rutgers install documentation, relating to 
license renewal and SASROOT relocation, is in 
/usr/local/SAS_8.2/doc/README.RUTGERS

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/SAS_8.2
