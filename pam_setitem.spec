Summary: pam_setitem PAM module
Name: pam_setitem
Version: 1.0
Release: 1
Copyright: Rutgers University
Group: System/Authentication
Source: ftp://rpm.rutgers.edu/rpm-packages/SOURCES/pam_setitem-%{version}.tar.gz
URL: http://oss.rutgers.edu/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Aaron Richton <richton@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: vpkg-SPROcc

%description
pam_setitem.so.1 is used to call the pam_set_item(3PAM) function from within 
the PAM stack as defined in pam.conf(4).
(from the man page)

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man5
mkdir -p $RPM_BUILD_ROOT/usr/lib/security
cp pam_setitem.so.1 $RPM_BUILD_ROOT/usr/lib/security
cp pam_setitem.5 $RPM_BUILD_ROOT/usr/local/man/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, bin) /usr/local/man/man5/pam_setitem.5
%attr(755, root, root) /usr/lib/security/pam_setitem.so.1
