Summary: Scheme shell
Name: scsh
Version: 0.5.2
Release: 2
Group: Development/Languages
Copyright: BSD-type
Source: scsh.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Scsh is a dialect of Scheme with I/O redirection, job control,
etc. and full access to Posix as well as common non-Posix extensions.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 ./configure --prefix=/usr/local --sysconfdir=/etc
touch .notify
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc


# Unfortunately, the doc directory is hardcoded in the Makefile.
rm -rf TMP-DOCS
mkdir TMP-DOCS
DESTDIR=`cd TMP-DOCS && pwd`
(cd $RPM_BUILD_ROOT/usr/local/lib/scsh/doc/ && find . -print | cpio -pmud \
    $DESTDIR)
rm -rf $RPM_BUILD_ROOT/usr/local/lib/scsh/doc

mv $RPM_BUILD_ROOT/usr/local/include/scheme48.h \
   $RPM_BUILD_ROOT/usr/local/include/scsh-scheme48.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc TMP-DOCS/*
/usr/local/bin/scsh
/usr/local/lib/scsh
/usr/local/include/scsh-scheme48.h
/usr/local/man/man1/scsh.1
