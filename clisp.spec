Name: clisp
Version: 2.26
Release: 2
Copyright: GPL
Group: Development/Languages
Summary: Common Lisp interpreter and compiler
Source: clisp-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
Clisp is a Common Lisp interpreter and compiler with a powerful
development environment.

%prep
%setup -q -n clisp-%{version}

%build
./configure solaris-rpm
cd solaris-rpm
./makemake --with-readline --with-gettext --with-dynamic-ffi > Makefile
make config.lisp
perl -i -p -e 's/edit\ config.lsp/Rutgers\ University/' config.lisp
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/locale
mkdir $RPM_BUILD_ROOT/usr/local/lib
mkdir $RPM_BUILD_ROOT/usr/local/man
mkdir $RPM_BUILD_ROOT/usr/local/bin
mkdir $RPM_BUILD_ROOT/usr/local/doc
cd solaris-rpm
make install DESTDIR=$RPM_BUILD_ROOT
umask 022

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/clisp
/usr/local/share/locale/*/LC_MESSAGES/clisp.mo
/usr/local/share/html/clisp.html
/usr/local/share/html/clreadline.html
/usr/local/share/dvi/clreadline.dvi
/usr/local/bin/clisp
/usr/local/man/man1/clisp.1
/usr/local/man/man3/clreadline.3
/usr/local/doc/clisp
