Name: spss
Summary: SPSS statistical package version 11.5.1
Version: 11.5.1
Release: 1
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
AutoReqProv: no

%description
SPSS statistical package version 11.5.1


%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT/usr/local
cd ..
cp -r spss-11.5.1 $RPM_BUILD_ROOT/usr/local

%post
cat <<EOF
Remember to update the license file!

To apply the license:

1. Change to the /bin subdirectory in the destination directory.
   cd /usr/local/spss-11.5.1/bin

2. Run the license script, licrenew. At the UNIX prompt type:
   ./licrenew.sh

3. Enter the license code that was included with your software.
   If you do not have this code, please contact root@nbcs.rutgers.edu.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/spss-11.5.1/*
