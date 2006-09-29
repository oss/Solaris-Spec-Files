Summary:	Creates tar archives
Name:		tar
Version:	1.15.91
Release:        1
Copyright:	GPL
Group:		System Environemtn/Base
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
GNU tar is an archiver that creates and handles file archives in various 
formats. You can use tar to create file archives, to extract files from 
previously created archives, store additional files, or update or list 
files which were already stored.

The program saves many files together into a single tape or disk 
archive, and can restore individual files from the archive. It includes 
multivolume support, the ability to archive sparse files, automatic 
archive compression/decompression, remote archives and special features 
that allow 'tar' to be used for incremental and full backups.

The supported archive formats are: V7 tar, GNU, ustar and POSIX (also 
known as pax interchange format). GNU tar can also read and extract 
'star' archives. Tar can direct its output to available devices, files, 
or other programs (using pipes); tar can even access remote devices or 
files (as archives). 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

make

make install DESTDIR=$RPM_BUILD_ROOT

%ifarch sparc64
LD_RUN_PATH="/usr/local/lib/sparcv9" \
CC="cc -xtarget=ultra -xarch=v9" CXX="CC -xtarget=ultra -xarch=v9" \
CPPFLAGS="-I/usr/local/include/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export LD_RUN_PATH CC CXX CPPFLAGS LDFLAGS
make clean
./configure --prefix=/usr/local
make 
%endif

%install
%ifarch sparc64
mkdir -p %{buildroot}/usr/local/bin/sparcv9
/usr/local/gnu/bin/install -c src/tar $RPM_BUILD_ROOT/usr/local/bin/sparcv9/tar
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --entry="* Tar: (tar).                   Making tape (or disk) archives." \
    /usr/local/info/tar.info
fi

if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    /usr/local/info/tar.info-1
fi

if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    /usr/local/info/tar.info-2
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --delete /usr/local/info/tsr.info
fi

if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --delete /usr/local/info/tsr.info-1
fi  

if [ -x /usr/local/bin/install-info ] ; then
    /usr/local/bin/install-info --info-dir="/usr/local/info" \
    --delete /usr/local/info/tsr.info-2
fi  

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/bin/sparcv9/*
/usr/local/libexec/rmt
/usr/local/sbin
/usr/local/info/tar.*

%changelog
* Fri Sep 29 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.15.91
- Bumped Version
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.15.90-1
- Updated to 1.15.90, created new spec file
