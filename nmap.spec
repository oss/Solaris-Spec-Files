%define name nmap
%define version 3.50
%define release 3
%define prefix /usr/local

# to not build the frontend, add:
#   --define "buildfe 0"
# ...to the rpm build command-line

%if "%{buildfe}" != "0"
%define buildfe 1
%endif

Summary: Network exploration tool and security scanner
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: http://www.insecure.org/nmap/dist/%{name}-%{version}.tgz
URL: http://www.insecure.org/nmap/
BuildRoot: %{_tmppath}/%{name}-root
Requires: openssl
# RPM can't be relocatable until I stop storing path info in the binary
# Prefix: %{prefix}

%description
Nmap is a utility for network exploration or security auditing. It
supports ping scanning (determine which hosts are up), many port
scanning techniques (determine what services the hosts are offering),
and TCP/IP fingerprinting (remote host operating system
identification). Nmap also offers flexible target and port
specification, decoy scanning, determination of TCP sequence
predictability characteristics, sunRPC scanning, reverse-identd
scanning, and more.

%if "%{buildfe}" == "1"
%package frontend
Summary: Gtk+ frontend for nmap
Group: Applications/System
Requires: nmap, gtk+
Version: 0.%{version}
%description frontend
This package includes nmapfe, a Gtk+ frontend for nmap. The nmap package must
be installed before installing nmap-frontend.
%endif

%prep
%setup -q

%build
PATH="/usr/sfw/bin:$PATH"
LD_RUN_PATH="/usr/lib /usr/local/lib" 
LD_LIBRARY_PATH="/usr/lib /usr/local/lib" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH LD_RUN_PATH LD_LIBRARY_PATH LDFLAGS

./configure --prefix=%{prefix} --with-ssl=/usr/local/ssl
make 

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Utilities

strip $RPM_BUILD_ROOT%{prefix}/bin/* || :
gzip $RPM_BUILD_ROOT%{prefix}/man/man1/* || :

%if "%{buildfe}" == "1"
%post frontend
rm -f ${prefix}/bin/xnmap
ln -s nmapfe ${prefix}/bin/xnmap
%endif

%if "%{buildfe}" == "1"
%postun frontend
rm -f ${prefix}/bin/xnmap
%endif

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc COPYING
%doc docs/README docs/copying.html docs/nmap-fingerprinting-article.txt
%doc docs/nmap.deprecated.txt docs/nmap.usage.txt docs/nmap_doc.html
%doc docs/nmap_manpage.html docs/nmap_manpage-es.html
%doc docs/nmap_manpage-fr.html docs/nmap_manpage-lt.html 
%doc docs/nmap_manpage-it.html
%doc docs/nmap_manpage-ru.html
%{prefix}/bin/nmap
%{prefix}/share/nmap
%{prefix}/man/man1/nmap.1.gz

%if "%{buildfe}" == "1"
%files frontend
%defattr(-,root,root)
%{prefix}/bin/nmapfe
%{prefix}/bin/xnmap
%{prefix}/share/gnome/apps/Utilities/nmapfe.desktop
%{prefix}/man/man1/xnmap.1.gz
%{prefix}/man/man1/nmapfe.1.gz
%endif

%changelog

* Wed Apr 03 2002 Aaron Richton <richton@nbcs.rutgers.edu>
Rutgers changes:
- we use /usr/local as prefix
- remove RPM_OPT_FLAGS from ./configure due to unavailable -m64 gcc2
- known bug: rpath not set properly for sunperl,gnome

* Fri Jun 01 2001 GOMEZ Henri (hgomez@slib.fr)
- Patch which checks that $RPM_BUILD_ROOT is not "/" before rm'ing it.

* Tue Mar 06 2001 Ben Reed <ben@opennms.org>
- changed spec to handle not building the frontend

* Thu Dec 30 1999 Fyodor <fyodor@insecure.org>
- Updated description
- Eliminated source1 (nmapfe.desktop) directive and simply packaged it with Nmap
- Fixed nmap distribution URL (source0)
- Added this .rpm to base Nmap distribution

* Mon Dec 13 1999 Tim Powers <timp@redhat.com>
- based on origional spec file from
	http://www.insecure.org/nmap/index.html#download
- general cleanups, removed lots of commenrts since it made the spec hard to
	read
- changed group to Applications/System
- quiet setup
- no need to create dirs in the install section, "make
	prefix=$RPM_BUILD_ROOT&{prefix} install" does this.
- using defined %{prefix}, %{version} etc. for easier/quicker maint.
- added docs
- gzip man pages
- strip after files have been installed into buildroot
- created separate package for the frontend so that Gtk+ isn't needed for the
	CLI nmap 
- not using -f in files section anymore, no need for it since there aren't that
	many files/dirs
- added desktop entry for gnome

* Sun Jan 10 1999 Fyodor <fyodor@insecure.org>
- Merged in spec file sent in by Ian Macdonald <ianmacd@xs4all.nl>

* Tue Dec 29 1998 Fyodor <fyodor@insecure.org>
- Made some changes, and merged in another .spec file sent in
  by Oren Tirosh <oren@hishome.net>

* Mon Dec 21 1998 Riku Meskanen <mesrik@cc.jyu.fi>
- initial build for RH 5.x










