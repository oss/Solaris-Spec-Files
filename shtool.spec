%include perl-header.spec

Summary: GNU shell tools
Name: shtool
Version: 1.5.1
Release: 2
Group: System Environment/Base
Copyright: GPL
Source: shtool-1.5.1.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
Shtool is a collection of shell scripts useful for distributions of
software.  If you are developing software that you plan to distribute,
using shtool may increase your portability, along with libtool and
autoconf.

%prep
%setup -q

%build
PATH="%{perl_prefix}/bin:$PATH" ./configure --prefix=/usr/local
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%post
cat <<EOF

Depending on your Perl installation, you may wish to change the first
line of shtoolize to read

  #!/usr/local/bin/perl

instead of

  #!/bin/perl

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING AUTHORS README THANKS
/usr/local/bin/shtool
/usr/local/bin/shtoolize
/usr/local/man/man1/shtool.1
/usr/local/man/man1/shtoolize.1
/usr/local/share/aclocal/shtool.m4
/usr/local/share/shtool
