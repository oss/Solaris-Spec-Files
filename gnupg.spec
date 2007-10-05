%include machine-header.spec

Summary:	GNU Privacy Guard
Name:		gnupg
Version:	1.4.7
Release:	2
Group:		Applications/Productivity
Copyright:	GPL
Source:		gnupg-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

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
	--disable-nls

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT mkinstalldirs=`pwd`/scripts/mkinstalldirs

rm -rf %{buildroot}/usr/local/share/info/dir

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
/usr/local/share/info/gnupg1.info
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

