%include machine-header.spec

Summary:	GNU Privacy Guard
Name:		gnupg
Version:	1.4.9
Release:	3
Group:		Applications/Productivity
License:	GPL
Source:		gnupg-%{version}.tar.gz
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Requires:	curl openssl bzip2 libiconv zlib openldap-lib >= 2.4
BuildRequires:	curl-devel openssl bzip2-devel libiconv-devel zlib-devel openldap-devel >= 2.4

%description 
GnuPG is GNUs tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/local/bin:$PATH"
CC="cc" CXX="CC" LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
CPPFLAGS="-I/usr/local/include"
export CC CXX PATH LD LDFLAGS CPPFLAGS 

./configure \
	--disable-nls \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot} mkinstalldirs=`pwd`/scripts/mkinstalldirs

rm -rf %{buildroot}/usr/local/info/dir

%post
if [ -x %{_bindir}/install-info ]; then
    %{_bindir}/install-info --info-dir=%{_infodir} \
        --entry="* gpg-%{version} (gnupg):     GNU Privacy Guard" \
        --section="Security" \
        %{_infodir}/gnupg1.info
fi

%preun
if [ -x %{_bindir}/install-info ]; then
    %{_bindir}/install-info --info-dir=%{_infodir} --delete \
        %{_infodir}/gnupg1.info
fi 

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc doc/ChangeLog doc/DETAILS doc/FAQ doc/HACKING
%doc README AUTHORS BUGS NEWS THANKS TODO
%{_infodir}/gnupg1.info
%{_datadir}/gnupg
%{_bindir}/*
%{_mandir}/man1/gpg*.1
%{_mandir}/man7/gnupg.7
%{_libexecdir}/gnupg

%changelog
* Mon Nov 17 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.4.9-3
- Fixed paths/info stuff
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.9-2
- Respin against openldap 2.4, added some Requires/BuildRequires
* Fri Jun 13 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.9-1
- Updated to version 1.4.9
* Wed Jan 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.8-1
- Updated to latest version

