Name:		rsync
Version:	3.0.3
Release:	1
License:	GPL 
Group:		Applications/Internet
Summary:	rsync is an open source utility that provides fast incremental file transfer. 
URL:		http://samba.anu.edu.au/rsync
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		rsync-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

%description
rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.
At first glance this may seem impossible because the calculation of
diffs between two files normally requires local access to both
files. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -xO4" CXX="CC -xO4" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=%{_prefix}	\
	--with-included-popt	\
	--mandir=%{_mandir}

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README COPYING NEWS OLDNEWS TODO
%{_bindir}/rsync
%{_mandir}/man1/rsync.1
%{_mandir}/man5/rsyncd.conf.5

%changelog
* Fri Aug 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.0.3-1
- Added doc entry, bumped to 3.0.3
* Tue Jun 10 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.0.2-1
- Updated to version 3.0.2
* Thu Oct 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0.0pre1
- Play bump
