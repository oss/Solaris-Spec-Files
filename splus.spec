Summary: S-Plus.
Name: splus
Version: 5.0
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
size in /usr/local: ~77MB

there is a 777 directory for licensing, /usr/local/SPLUS/adm/lic/logs

after installing, read and follow the instructions in:
    /usr/local/SPLUS/RU.README

note that this is licensed software, you will need to obtain a license key
from SPLUS.  You do this by running a command and sending the info to: 
	ssr@statsci.com or fax to (206) 283-8691

for details on this licensing command, again, see:
	 /usr/local/SPLUS/RU.README 


%prep
%setup -q

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

cd $build_dir/files
find . -print | cpio -pdmuv $RPM_BUILD_ROOT

%post
cat <<EOF
size in /usr/local: ~77MB

there is a 777 directory for licensing, /usr/local/SPLUS/adm/lic/logs

after installing, read and follow the instructions in:
    /usr/local/SPLUS/RU.README

note that this is licensed software, you will need to obtain a license key
from SPLUS.  You do this by running a command and sending the info to: 
	ssr@statsci.com or fax to (206) 283-8691

for details on this licensing command, again, see:
	 /usr/local/SPLUS/RU.README 

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/SPLUS
/usr/local/man/man*/*
