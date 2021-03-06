Name:		tar
Version:	1.26
Release:        2
License:	GPL
Group:		System Environment/Base
URL:		http://www.gnu.org/software/tar
Source:		ftp://ftp.gnu.org/gnu/tar/tar-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:	The GNU Tar archiver

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
%configure --disable-nls --disable-silent-rules

gmake -j3


%install
gmake install DESTDIR=%{buildroot}
%ifarch sparc64
%{__install} -D src/tar %{buildroot}%{_bindir}/sparcv9/tar
%endif

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/tar.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/tar.info
fi

%files
%defattr(-, root, root, -)
%doc README COPYING AUTHORS THANKS
%doc NEWS ChangeLog* TODO PORTS
%{_bindir}/tar
%{_bindir}/sparcv9/tar
%{_libexecdir}/rmt
%{_infodir}/*

%changelog
* Tue Feb 12 2013 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 1.26-2
- Release bump to test publish scripts
* Fri Aug 19 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 1.26-1
- Update to 1.26
* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.23-1
- Updated to 1.23
* Fri Jul 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.22-1
- Updated to version 1.22
- Added tar-1.22-inttypes.patch, needed for 64-bit build
- Fixed doc permissions
* Tue Jan 06 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.21-1
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
