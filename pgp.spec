Name: pgp
Version: 2.6.2s
Release: 2
Summary: Phil Zimmerman's "Pretty Good Privacy"
License: Free to use, distribution restricted
Group: Applications/Productivity
BuildRoot: /var/tmp/%{name}-root
Source: pgp262s.tar.gz

%description
PGP is a widely-used encryption program capable of encrypting and
digitally signing data.  This program has some extensive restrictions
on its redistribution; read the license documents carefully.

Bear in mind that you have to create a ~/.pgp directory before you
create your private key, and it shouldn't be world-readable.

%prep
%setup -c -T -n pgp
%setup -D -T -a 0 -n pgp
tar xf pgp262si.tar
tar xf rsaref.tar

%build
(cd rsaref/install/unix && make)
(cd src && make sun4sunos5gcc)

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/pgp
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
install -c -m 0755 src/pgp $RPM_BUILD_ROOT/usr/local/bin/pgp
install -c -m 0755 doc/pgp.1 $RPM_BUILD_ROOT/usr/local/man/man1/pgp.1
for i in config.txt language.txt *hlp ; do
    install -c -m 0644 $i $RPM_BUILD_ROOT/usr/local/lib/pgp/$i
done

%clean
rm -rf %RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*txt doc/*doc rsalicen.txt mitlicen.txt readme.doc
/usr/local/bin/pgp
/usr/local/man/man1/pgp.1
/usr/local/lib/pgp


