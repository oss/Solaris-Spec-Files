Name: fastfs
Version: 1.3
Release: 1
Summary: fastfs
Copyright: Redistributable
Group: Utilities/System
Source0: fastfs-1.3.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}


%description
Note that it is intended for use with restore(8)
to speed up full filesystem restores. Remember
that if a filesystem is running with delayed I/O
enabled when the system crashes it can result in
fsck being unable to "fix" the filesystem on reboot
without manual intervention.


%prep
%setup -q

%build

gcc fastfs.c

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 a.out $RPM_BUILD_ROOT/usr/local/sbin/fastfs


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
/usr/local/sbin/fastfs

