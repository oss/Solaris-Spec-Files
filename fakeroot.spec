Summary: Fake root access for package creation
Name: fakeroot
Version: 0.9.0
Release: 1
Copyright: GPL
Group: Applications/Archiving
Source: fakeroot_%{version}.tar.gz
Patch: fakeroot.patch
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
Fakeroot runs a command in an environment were it appears to have root
privileges for file manipulation, by setting LD_PRELOAD to a library with 
alternative versions of getuid(), stat(), etc. This is useful for allowing 
users to create archives (tar, ar, .deb .rpm etc.) with files in them with
root permissions/ownership. Without fakeroot one would have to have root 
privileges to create the constituent files of the archives with the correct 
permissions and ownership, and then pack them up, or one would have to 
construct the archives directly, without using the archiver. 

%prep
%setup -q
%patch -p1 

%build 
./configure --prefix=/usr/local

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/bin/*
/usr/local/lib/*
/usr/local/man/man1/*










