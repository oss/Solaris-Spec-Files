Summary:	An antivirus for Unix
Name:		clamav
Version:	0.65
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://clamav.sf.net/stable/%{name}-%{version}.tar.gz
URL:		http://clamav.sf.net/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRequires:	autoconf automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Clam AntiVirus is an powerful anti-virus toolkit for Unix.
The package provides a flexible and scalable multi-threaded daemon,
a command line scanner, and a tool for automatic updating via Internet.
It supports AMaViS, Sendmail milter, compressed files and mbox format.
Clamav is multithreaded, written in C, and POSIX compliant.

%prep
%setup -q

%build
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"
CC="gcc -03 -pipe -s -fforce-addr"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

./configure \
	--enable-id-check \
	--disable-clamav \
	--with-user=clamav \
	--with-group=clamav \
	--with-dbdir=%{_localstatedir}/lib/clamav \
	--sysconfdir=/etc

make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#Not done at Rutgers.
#%pre
#	/usr/sbin/groupadd -g 46 -r -f clamav
#	/usr/sbin/useradd -u 46 -r -d /tmp  -s /sbin/nologin -c "Clam AV Checker" -g clamav clamav 1>&2

%post
cat <<EOF

To complete installation, make sure you create some sort of clamav user and group.

EOF

%files
%defattr(0644,root,root,0755)
%doc AUTHORS BUGS COPYING ChangeLog FAQ INSTALL NEWS README TODO docs/html/
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/clamd
%attr(0755,root,root) %{_libdir}/libclamav.so.*
%attr(0755,root,root) %dir %{_localstatedir}/lib/clamav/
%attr(0644,root,root) %{_localstatedir}/lib/clamav/mirrors.txt
%attr(0644,root,root) %{_localstatedir}/lib/clamav/main.cvd
%attr(0644,root,root) %{_localstatedir}/lib/clamav/daily.cvd
%{_mandir}/man1/clamdscan.1*
%{_mandir}/man1/clamscan.1*
%{_mandir}/man1/freshclam.1*
%{_mandir}/man1/sigtool.1*
%{_mandir}/man5/clamav.conf.5*
%{_mandir}/man8/clamd.8*


%changelog
* Mon Dec 22 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Rutgerized package.
* Wed Dec 03 2003 Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Initial Rutgers release


