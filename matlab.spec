Summary: matrix based math program for scientists and engineers
Name: matlab
Version: 5.3.1.29215a
Release: 2
Group: Licensed
Copyright: Licensed
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tar

%description
http://www.mathworks.com/


INSTALLATION: 

o cd /usr/local/matlab5/etc

o cp -p license.dat.example license.dat

o Edit the following line:  

SERVER |>HOSTNAME<| |>HOST_ID<| 1705

replacing |>HOSTNAME<| with the output of /usr/bin/hostname 
replacing |>HOST_ID<|  with the output of /usr/bin/hostid 

Example:  

SERVER gladsheim.rutgers.edu 809281a1 1711

o Invoke the program with the command 

/usr/local/bin/matlab 


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
http://www.mathworks.com/


INSTALLATION: 

o cd /usr/local/matlab5/etc

o cp -p license.dat.example license.dat

o Edit the following line:  

SERVER |>HOSTNAME<| |>HOST_ID<| 1705

replacing |>HOSTNAME<| with the output of /usr/bin/hostname 
replacing |>HOST_ID<|  with the output of /usr/bin/hostid 

Example:  

SERVER gladsheim.rutgers.edu 809281a1 1711

o Invoke the program with the command 

/usr/local/bin/matlab 

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/matlab5
/usr/local/bin/*
