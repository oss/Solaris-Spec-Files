%define _sysconfdir /usr/local/etc

Name: apt
Version: 0.5.4cnc8
Release: 0.999ru
Summary: Debian's Advanced Packaging Tool with RPM support
Summary(pt_BR): Frontend avançado para pacotes rpm e deb
Summary(es): Advanced Packaging Tool frontend for rpm and dpkg
Group: Administration
Group(pt_BR): Administração
Group(es): Administración
License: GPL
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}-0.5.4.conf
Source2: vendors.list
Source3: apt.sourceslist.sh
Source4: apt-apt-checkrpm
Requires: rpm >= 4.1
Requires: bzip2
BuildRequires: rpm-devel >= 4.1, bzip2, gnupg, fileutils, patch
%ifnos solaris2.9
BuildRequires: zlib-devel
%endif
BuildRoot: %{_tmppath}/%{name}-root
Patch: apt-0.5.4cnc8-solaris-2.patch

%description
A port of Debian's apt tools for RPM based distributions,
or at least for Conectiva. It provides the apt-get utility that
enables a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source
capability and several other unique features.

Modified for solaris toolchain w/o glibc.  ASM - Rutgers U. 
There are a few hacks.  Also made changes to have all file 
locations specified in apt.conf.

%description -l pt_BR
Um porte das ferramentas APT do Debian para distribuições 
baseadas em RPM. Provê o utilitário apt-get, que habilita uma forma
mais simples e segura para instalar e atualizar pacotes.

%package server-tools
Requires: apt >= 0.5.4cnc7
Requires: fileutils
Group: Administration
Summary: Tools to build an "apt-able" repository. 

%description server-tools
Tools needed to publish a repositiory of RPM's so they are accessible to apt.

%prep
%setup -q
%patch -p1


PATH="/usr/local/gnu/bin:$PATH"
export PATH

%build
LD_LIBRARY_PATH="/usr/local/lib" \
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/include/rpm"  \
CXXFLAGS="-L/usr/local/lib -R/usr/local/lib" \
INSTALL="/usr/local/gnu/bin/install" \
./configure --prefix=/usr/local --exec-prefix=/usr/local \
 --sysconfdir=/usr/local/etc --disable-nls

make NOISY=1

%install
# clean out dir where everything will be installed
rm -fr %{buildroot}

# working dirs "var"
mkdir -p %{buildroot}/var/local/cache/%{name}/archives/partial
mkdir -p %{buildroot}/var/local/cache/%{name}/genpkglist
mkdir -p %{buildroot}/var/local/cache/%{name}/gensrclist
mkdir -p %{buildroot}/var/local/lib/rpm/status
mkdir -p %{buildroot}/var/local/state/%{name}/lists/partial

# executables
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}/usr/local/lib/
cp -r bin/* %{buildroot}%{_bindir}/
mv %{buildroot}%{_bindir}/*.so* %{buildroot}/usr/local/lib/

install tools/genbasedir %{buildroot}%{_bindir}/genbasedir

# config files "etc"
mkdir -p %{buildroot}/usr/local/etc/apt

# START: CHRIS'S sources.list hacking
bash %{_sourcedir}/apt.sourceslist.sh > %{buildroot}/usr/local/etc/apt/sources.list
# END: CHRIS'S sources.list hacking
#%ifos solaris2.9
#sed "/gzip/d" %{_sourcedir}/%{name}-0.5.4.conf > %{buildroot}/usr/local/etc/apt/apt.conf
#%else
cp %{_sourcedir}/%{name}-0.5.4.conf %{buildroot}/usr/local/etc/apt/apt.conf
#%endif


#install %{_sourcedir}/%{name}.conf %{buildroot}%{_sysconfdir}/apt/apt.conf
install %{_sourcedir}/vendors.list %{buildroot}%{_sysconfdir}/apt/vendors.list
install rpmpriorities %{buildroot}%{_sysconfdir}/apt/rpmpriorities

# "include"
mkdir -p %{buildroot}%{_includedir}/apt-pkg/
install apt-pkg/*.h %{buildroot}%{_includedir}/apt-pkg/
install apt-pkg/*/*.h %{buildroot}%{_includedir}/apt-pkg/

# helper methods for apt: ftp, http, ...
mkdir -p %{buildroot}%{_libdir}/apt/methods
install  bin/methods/* %{buildroot}%{_libdir}/apt/methods

#docs
mkdir -p %{buildroot}/%{_mandir}/man5/
mkdir -p %{buildroot}/%{_mandir}/man8/
install doc/apt.conf.5 %{buildroot}/%{_mandir}/man5/apt.conf.5
install doc/sources.list.5 %{buildroot}/%{_mandir}/man5/sources.list.5
install doc/vendors.list.5 %{buildroot}/%{_mandir}/man5/vendors.list.5
install doc/apt-cache.8 %{buildroot}/%{_mandir}/man8/apt-cache.8
install doc/apt-config.8 %{buildroot}/%{_mandir}/man8/apt-config.8
install doc/apt.8 %{buildroot}/%{_mandir}/man8/apt.8
install doc/apt-cdrom.8 %{buildroot}/%{_mandir}/man8/apt-cdrom.8
install doc/apt-get.8 %{buildroot}/%{_mandir}/man8/apt-get.8

cp %{SOURCE4} %{buildroot}/usr/local/bin/apt-checkrpm
chmod 755 %{buildroot}/usr/local/bin/apt-checkrpm

# wacky international stuff
#mkdir -p %{buildroot}%{_libdir}/locale
#mkdir -p %{buildroot}%{_datadir}/locale
#(cd po;make install DESTDIR=%{buildroot})

%post
if [ -d /etc/apt ]; then
mv /etc/apt /etc/apt.old
echo /etc/apt renamed to /etc/apt.old, /usr/local/etc/apt is used now
fi


%clean
rm -rf %{buildroot}

%files 
%defattr(0644, root, bin, 755) 
%doc COPYING* README* TODO 
#%doc docs/examples/configure-index 
#%doc docs/examples/vendors.list 
#%doc docs/examples/sources.list 
%config() /usr/local/etc/apt/apt.conf
%config() /usr/local/etc/apt/rpmpriorities
%config(noreplace) /usr/local/etc/apt/sources.list
%config() /usr/local/etc/apt/vendors.list
%{_mandir}/man5/* 
%{_mandir}/man8/* 
/var/local
%defattr(755,root,root) 
/usr/local/lib/*.so*
/usr/local/lib/apt/*
%{_bindir}/apt*

# repository stuff
%files server-tools
%defattr(0644, root, bin)
#%dir %{_localstatedir}/cache/apt/genpkglist
#%dir %{_localstatedir}/cache/apt/gensrclist
%defattr(0755, root, bin)
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_bindir}/hdlist2pkglist
%{_bindir}/genbasedir


%changelog
* Thu Dec 13 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
+ apt-0.3.19cnc38-9ru
- added dependency information to apt-server-tools
- added Austin's genbasedir
- changed sample sources.list, post-install message

* Tue Jul 31 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
+ apt.0.3.19cnc38-6ru
- fixed file ownership problems

* Tue Jul 17 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
+ apt.0.3.19cnc38-5ru
- moved patches to apt.*
- removed configure.in patch
- build against, link to rpm 4.0.2 instead of 3.0.5
- fixed solaris 2.6 build
- removed message for LD_LIBRARY_PATH

* Tue Jun 26 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
+ apt.0.3.19cnc38-4ru
- clean up patches
- no more mangles (qsort)
- build procedure w/o ac 

* Tue Jun 19 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
+ apt.0.3.19cnc38-3ru
- stopped config file stomping
- removed aclocal.m4 patch
- cleaned up spec file

* Tue Jun 13 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
+ apt.0.3.19cnc38-2ru
- separated client and server portions

* Tue May 29 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
+ apt-0.3.19cnc38-1ru
- rutgers specific config files
- works "out of the box"

* Tue May 29 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
- removed devel sections
- move apt into /usr/local/*  instead of /*
- reworked the install and files sections

* Tue May 22 2001 Austin S. Murphy <amurphy@eden.rutgers.edu>
- mod'd to work on Solaris 2.7 w/o glibc
- client works fine, server prep not as nice
- qsort does not work in genpkglist
- code for scandir() and alphasort() copied from glibc into genpkglist
- setenv() statements commented out in genpkglist, gensrclist, hdlist2pkglist
- unsetenv() commented out in gpg (may disable gpg)

* Thu Mar 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc38-2cl
- autotester workaround...

* Thu Mar 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc38-1cl
- released version 0.3.19cnc38
- fixed epoch display on apt-cache
- added user specified public keyring option for gpg 
- added italian po file
- fixed bug on dependency resolution for virtual packages with mult.providers

* Tue Feb 20 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc37-1cl
- released version 0.3.19cnc37
- noreplace put back for sources.list (closes: #1548)
- recompiled (closes: #1559)
- fixed dist-upgrade bogus msg (closes: #1254)
- fixed no_proxy handling

* Sat Feb 17 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ apt-0.3.19cnc36-1cl
- released version 0.3.19cnc36
- fixed problem with arch selection (I swear it works now!)
- fixed bug with rpm4

* Wed Feb 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc35
- fixed problem with case sensitiveness
- fixed rpmpriority interpretation

* Wed Feb 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc34
- rpm4 fix?

* Wed Jan 24 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc33
- added new gui hookz

* Sat Jan 20 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc32
- fixed arch selection code
- fixed priority and section info in internal package structs

* Tue Jan 16 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- unbroke potfiles

* Mon Jan 15 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc31

* Mon Jan 15 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc30

* Sat Jan 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc29

* Thu Jan 04 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc28
- added gnupg dependency

* Thu Dec 07 2000 Andreas Hasenack <andreas@conectiva.com>
- damn! Wrong URL in sources.list, atualizacoes.conectiva.com
  doesn't exist, of course...

* Thu Dec 07 2000 Andreas Hasenack <andreas@conectiva.com>
- updated sources.list with new mirrors and new download tree
- removed (noreplace) for the sources.list file for this
  upgrade. It will be easier for the user. The (noreplace)
  should be back in place after this update as we expect no
  further big modifications for that file, only new mirrors.

* Wed Dec 06 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- fixed prob in vendors.list

* Tue Dec 05 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc27

* Wed Nov 08 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc26

* Mon Nov 06 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc25

* Thu Nov 02 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc24

* Thu Nov 02 2000 Rud<E1> Moura <ruda@conectiva.com>
- updated source.list (again)

* Thu Nov 02 2000 Rud<E1> Moura <ruda@conectiva.com>
- updated source.list

* Wed Nov 01 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc23
- added cache directories for gen{pkg,src}list
- pt_BR manpages

* Tue Oct 31 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc22
- Requires -> PreReq in apt-devel

* Mon Oct 30 2000 Alfredo Kojima <kojima@conectiva.com>
- collapsed libapt-pkg-devel and -doc to apt-devel

* Mon Oct 30 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc21

* Sun Oct 29 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc20

* Sun Oct 29 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc19
- added gensrclist
- support for apt-get source

* Fri Oct 27 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc18

* Thu Oct 26 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc17
- new manpages

* Wed Oct 25 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc16

* Sun Oct 22 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc15

* Sat Oct 21 2000 Alfredo K. Kojima <kojima@conectiva.com.br>
- released version 0.3.19cnc14

* Thu Oct 19 2000 Claudio Matsuoka <claudio@conectiva.com>
- new upstream release: 0.3.9cnc13

* Tue Oct 17 2000 Eliphas Levy Theodoro <eliphas@conectiva.com>
- added rpmpriorities to filelist and install

* Tue Oct 17 2000 Claudio Matsuoka <claudio@conectiva.com>
- updated to 0.3.19cnc12
- fresh CVS snapshot including: support to Acquire::ComprExtension,
  debug messages removed, fixed apt-cdrom, RPM DB path, rpmlib call
  in pkgRpmLock::Close(), package priority kludge removed, i18n
  improvements, and genbasedir/genpkglist updates.
- handling language setting in genpkglist to make aptitude happy

* Wed Oct 11 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc11
- fixed problem with shard lib symlinks

* Tue Oct 10 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc10

* Mon Oct  2 2000 Claudio Matsuoka <claudio@conectiva.com>
- fixed brown paper bag bug with method permissions
- added parameter --sign to genbasedir
- added html/text doc files

* Sat Sep 30 2000 Claudio Matsuoka <claudio@conectiva.com>
- bumped to 0.3.19cnc9
- added vendors.list
- added gpg method
- fixed minor stuff to make Aptitude work
- added missing manpages
- fixed shared libs
- split in apt, libapt-pkg, libapt-pkg-devel, libapt-pkg-doc
- rewrote genbasedir in shell script (original was in TCL)
- misc cosmetic changes

* Tue Sep 26 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc8

* Wed Sep 20 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc7

* Mon Sep 18 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc6

* Sat Sep 16 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc5

* Fri Sep 15 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc4

* Mon Sep 12 2000 Alfredo K. Kojima <kojima@conectiva.com>
- released version 0.3.19cnc3

* Mon Sep 5 2000 Alfredo K. Kojima <kojima@conectiva.com>
- renamed package to apt, with version 0.3.19cncV

* Mon Sep 5 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.10
- added genpkglist and rapt-config
- program names changed back to apt-*

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.9

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.8

* Mon Sep 4 2000 Alfredo K. Kojima <kojima@conectiva.com>
- 0.7

* Fri Sep 1 2000 Alfredo K. Kojima <kojima@conectiva.com>
- fixed typo in sources.list

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.6

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.5

* Tue Aug 31 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.4

* Wed Aug 30 2000 Alfredo K. Kojima <kojima@conectiva.com>
- version 0.3

* Thu Aug 28 2000 Alfredo K. Kojima <kojima@conectiva.com>
- second try. new release with direct hdlist handling

* Thu Aug 10 2000 Alfredo K. Kojima <kojima@conectiva.com>
- initial package creation. Yeah, it's totally broken for sure.

