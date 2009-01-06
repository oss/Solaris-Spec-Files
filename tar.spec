Summary:	Creates tar archives
Name:		tar
Version:	1.21
Release:        1
License:	GPL
Group:		System Environment/Base
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
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

./configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--disable-nls

gmake -j3

gmake install DESTDIR=$RPM_BUILD_ROOT

%ifarch sparc64
LD_RUN_PATH="/usr/local/lib/sparcv9" \
CC="cc -xtarget=ultra -xarch=v9" CXX="CC -xtarget=ultra -xarch=v9" \
CPPFLAGS="-I/usr/local/include/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export LD_RUN_PATH CC CXX CPPFLAGS LDFLAGS
gmake clean
./configure --prefix=%{_prefix} --infodir=%{_infodir} --disable-nls
gmake -j3 
%endif

%install
%ifarch sparc64
%{__install} -d $RPM_BUILD_ROOT%{_bindir}/sparcv9
%{__install} src/tar $RPM_BUILD_ROOT%{_bindir}/sparcv9/tar
%endif

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} \
    --entry="* Tar: (tar).                   Making tape (or disk) archives." \
    %{_infodir}/tar.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} \
    --delete %{_infodir}/tar.info
fi

%files
%doc README AUTHORS COPYING NEWS TODO PORTS THANKS ChangeLog*
%defattr(-,bin,bin)
%{_bindir}/*
%{_libexecdir}/rmt
%{_infodir}/*

%changelog
* Tue Jan 06 2009 Brian Schubert <schubert@nbcs.rutgers.edu> 1.21-1
- Updated to version 1.21, made a few minor changes to the spec file.
* Thu Jul 31 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.20-2
- fixed info issues
- added doc section
* Thu Apr 24 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.20-1
- bumped to 1.20, removed charset.alias file
* Fri Oct 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.19-1
- Bump tp 1.19
* Fri Sep 29 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.15.91
- Bumped Version
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.15.90-1
- Updated to 1.15.90, created new spec file
