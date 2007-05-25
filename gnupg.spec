%include machine-header.spec

Summary: GNU Privacy Guard
Name: gnupg
Version: 1.4.7
Release: 1
Group: Applications/Productivity
Copyright: GPL
Source: gnupg-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
%ifnos solaris2.9
Requires: egd
%endif

%description 
GnuPG is GNUs tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/local/bin:$PATH"
CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
%ifos solaris2.9
  CPPFLAGS="-I/usr/local/include" ./configure
%else
  CPPFLAGS="-I/usr/local/include" ./configure --enable-static-rnd=egd
%endif
export CC CXX PATH LD LDFLAGS CPPFLAGS 
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT mkinstalldirs=`pwd`/scripts/mkinstalldirs


%post
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/info \
        --entry="* gpg-%{version} (gnupg):     GNU Privacy Guard" \
        --section="Security" \
        /usr/local/info/gpg.info
fi

if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/info \
        --entry="* gpgv-%{version} (gnupg):     GNU Privacy Guard" \
        --section="Security" \
        /usr/local/info/gpgv.info
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/info --delete \
        /usr/local/info/gpg.info
fi 

if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --info-dir=/usr/local/info --delete \
        /usr/local/info/gpgv.info
fi 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/ChangeLog doc/DETAILS doc/FAQ doc/HACKING
%doc README AUTHORS BUGS NEWS THANKS TODO
#/usr/local/lib/gnupg
/usr/local/share/info/gnupg1.info
/usr/local/share/info/dir
/usr/local/share/locale/*/LC_MESSAGES/gnupg.mo
/usr/local/share/gnupg/*
/usr/local/bin/*
/usr/local/share/man/man1/gpg.1
/usr/local/share/man/man1/gpgv.1
/usr/local/share/man/man1/gpg.ru.1
/usr/local/share/man/man7/gnupg.7
/usr/local/libexec/gnupg/gpgkeys_curl
/usr/local/libexec/gnupg/gpgkeys_finger
/usr/local/libexec/gnupg/gpgkeys_hkp
/usr/local/libexec/gnupg/gpgkeys_ldap

