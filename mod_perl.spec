%include perl-header.spec
%define defperlver 5.6.1
%define perlver %(rpm -q perl --queryformat '%%{version}' 2> /dev/null || echo %{defperlver})
%define perlmajor %(echo %{perlver} | cut -f1 -d.)
%define contentdir /var/www
%define _libdir %{perl_prefix}/lib
%define _prefix %{perl_prefix}
%define apver 1.3.26

Summary: An embedded Perl interpreter for the Apache Web server.
Name: mod_perl
Version: 1.27
Release: %{apver}_1
Group: System Environment/Daemons
Source0: http://perl.apache.org/dist/mod_perl-%{version}.tar.gz
License: GPL
URL: http://perl.apache.org/
BuildRoot: %{_tmppath}/%{name}-root
Requires: webserver, perl = %{perlver}, apache = %{apver}
BuildPrereq: apache-devel = %{apver}, perl
Prereq: perl

%description
Mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.
Mod_perl links the Perl runtime library into the Apache web server and
provides an object-oriented Perl interface for Apache's C language
API.  The end result is a quicker CGI script turnaround process, since
no external Perl interpreter has to be started.

Install mod_perl if you're installing the Apache web server and you'd
like for it to directly incorporate a Perl interpreter.

%prep
%setup -q

PATH="$PATH:/usr/local/perl5/bin/"
export PATH

%build
# Compile the module.
PATH="$PATH:/usr/local/perl5/bin/"
export PATH
perl Makefile.PL \
	USE_APXS=1 WITH_APXS=/usr/local/apache-%{apver}/bin/apxs PERL_USELARGEFILES=0 \
	EVERYTHING=1 
	#CCFLAGS="$RPM_OPT_FLAGS -fPIC"
make

# Run the test suite.
make test

%install
PATH="$PATH:/usr/local/perl5/bin/"
export PATH

#[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make "PREFIX=$RPM_BUILD_ROOT%{_prefix}" pure_install 

# Install the module itself.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/apache
install -c -m 755 apaci/libperl.so $RPM_BUILD_ROOT%{_libdir}/apache/

# Install its manual.
mkdir -p $RPM_BUILD_ROOT%{contentdir}/html/manual/mod/mod_perl
install -c -m 644 htdocs/manual/mod/mod_perl.html \
        $RPM_BUILD_ROOT%{contentdir}/html/manual/mod

make -C faq
rm faq/pod2htm*
install -m644 faq/*.html $RPM_BUILD_ROOT%{contentdir}/html/manual/mod/mod_perl/

# Remove the temporary files.
find $RPM_BUILD_ROOT%{_libdir}/site_perl/*/*/auto -name "*.bs" | xargs rm
rm   $RPM_BUILD_ROOT%{_libdir}/site_perl/*/*/auto/%{name}/.packlist

mkdir -p $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec
mv $RPM_BUILD_ROOT%{_libdir}/apache/libperl.so $RPM_BUILD_ROOT/usr/local/apache-%{apver}/libexec

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS Changes README SUPPORT ToDo cgi_to_mod_perl.pod mod_perl.pod
%doc mod_perl_method_handlers.pod mod_perl_traps.pod mod_perl_tuning.pod
%doc INSTALL faq/*.html eg faq
%doc ToDo apache-modlist.html
%{contentdir}/html/manual/mod/*
/usr/local/apache-%{apver}/libexec/libperl.so
%{_libdir}/site_perl/*/*/auto/*
%{_libdir}/site_perl/*/*/Apache*
%{_libdir}/site_perl/*/*/Bundle/*
%{_libdir}/site_perl/*/*/cgi*
%{_libdir}/site_perl/*/*/mod_perl*
%{_mandir}/man3/*.3*

%changelog
* Fri Feb  8 2002 Nalin Dahyabhai <nalin@redhat.com> 1.26-3
- rebuild

* Thu Jan 31 2002 Nalin Dahyabhai <nalin@redhat.com> 1.26-2
- turn off large file support, which makes mod_perl think that server request
  structures are the wrong size (heads-up from Doug MacEachern and Chip Turner)

* Wed Jan 23 2002 Nalin Dahyabhai <nalin@redhat.com> 1.26-1
- update to 1.26

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.24_01-4
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com> 1.24_01-3
- Bump release + rebuild.

* Tue Feb 27 2001 Nalin Dahyabhai <nalin@redhat.com> 1.24_01-2
- don't include .bs files

* Sat Jan 20 2001 Nalin Dahyabhai <nalin@redhat.com> 1.24_01-1
- update to 1.24_01
- add URL

* Fri Nov 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Fri Aug 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch to fix bug in Apache::ExtUtils (#17147)

* Mon Jul 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove backup files from docs (#14174)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove workarounds for broken Perl

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- get rid of multiple prefixes

* Wed May 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.24
- remove pre- and post-install scripts and triggers

* Thu May 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- work around weird Perl version reporting problems with a suitably weird check

* Fri Apr 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify to be able to rebuild on both 5.003 and 5.6.0
- update to 1.23

* Thu Mar 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with perl 5.6.0
- add perlver macro to spec file to make handling of other perl versions easier

* Thu Mar 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.22

* Fri Mar 03 2000 Cristian Gafton <gafton@redhat.com>
- fixed the postun script to check for upgrades. doh
- add triggerpostun to fix older versions of the package

* Mon Feb 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- make perl a prereq because it's used in %post

* Fri Feb 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild against Apache 1.3.12 and EAPI (release 8)

* Mon Feb 21 2000 Preston Brown <pbrown@redhat.com>
- incorporate fixes from Markus Pilzecker <mp@rhein-neckar.netsurf.de>:
- Prefix: /usr
- find apxs binary and package directories automatically

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- automatically enable/disable in httpd.conf in post/postun.

* Thu Feb 10 2000 Preston Brown <pbrown@redhat.com>
- fix up some strange permissions

* Sun Feb 06 2000 Preston Brown <pbrown@redhat.com>
- rebuild to pick up gzipped man pages, new descr.

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- changed paths for perl 5.00503 (RHL 6.1 version)

* Fri Jul 09 1999 Preston Brown <pbrown@redhat.com>
- added -fPIC to correct functionality on SPARC
- upgrade to 1.21, removed build cruft from old buggy mod_perl days
- added extra documentation that was missing

* Fri Apr 16 1999 Preston Brown <pbrown@redhat.com>
- bump ver. # so SWS mod_perl gets auto-upgraded

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- bugfix 1.19 release from Doug

* Wed Mar 24 1999 Preston Brown <pbrown@redhat.com>
- experimental patch from Doug MacEachern <dougm@pobox.com> to fix segfault
- rebuilt against apache 1.3.6

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- upgraded to mod_perl 1.18.

* Mon Dec 21 1998 Preston Brown <pbrown@redhat.com>
- Upgraded to mod_perl 1.16.

* Thu Sep 03 1998 Preston Brown <pbrown@redhat.com>
- disabled stacked_handlers.  They still seem busted!
- minor updates so no conflicts with either apache / secureweb
- fixed bug building on multiple architectures

* Wed Sep 02 1998 Preston Brown <pbrown@redhat.com>
- Updates for apache 1.3.x, and mod_perl 1.15

* Fri Feb 27 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to compile it as a shared object for the apache/ssl (and
  future revisions of apache)

