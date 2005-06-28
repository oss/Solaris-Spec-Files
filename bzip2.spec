Name: bzip2
Version: 1.0.3
Copyright: BSD type
Group: Applications/Archiving
Summary: The bzip2 compression program
Release: 1
Source: bzip2-1.0.3.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Vendor: NBCS-OSS
Packager: Hardik Varia <hvaria@nbcs.rutgers.edu>
%description
Bzip2 is a lossless compression program.  It is slightly slower than
gzip, but it achieves better compression.  This package also includes the
libbz2.a library, if you wish to include bzip2 compression in a program.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install PREFIX=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/bzip2
/usr/local/bin/bunzip2
/usr/local/bin/bzcat
/usr/local/bin/bzip2recover
/usr/local/lib/libbz2.a
/usr/local/man/man1/bzip2.1
/usr/local/include/bzlib.h
