Summary: GNU Privacy Guard
Name: gnupg
Version: 1.0.6
Release: 2
Group: Applications/Productivity
Copyright: GPL
Source: gnupg-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: egd

%description 
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" ./configure --enable-static-rnd=egd
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/gpg.sgml doc/ChangeLog doc/DETAILS doc/FAQ doc/HACKING
%doc README AUTHORS BUGS NEWS THANKS TODO
/usr/local/lib/gnupg
/usr/local/share/locale/*/LC_MESSAGES/gnupg.mo
/usr/local/bin/gpg
/usr/local/share/gnupg/options.skel
/usr/local/man/man1/gpg.1
