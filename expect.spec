%define tcl_ver 8.3.1

Name: expect
Version: 5.32
Copyright: BSD-like
Group: Development/Tools
Summary: A tool for writing interactive scripts
Release: 3
Source: expect.tar.gz
BuildRoot: /var/tmp/%{name}-root
%ifos solaris2.9
Requires: vpkg-SUNWTcl
BuildRequires: vpkg-SUNWTcl
%else
Requires: tcl tcl-tk
BuildRequires: tcl-headers
%endif

%description
Expect lets you write scripts to automate interactive processes.  

%prep
%setup -q

%build
./configure --prefix=/usr/local --enable-shared --enable-gcc \
    --with-tclinclude=/usr/local/src/tcl-%{tcl_ver}/generic
ed Makefile <<__EOTEXT__
    /\/usr\/ccs\/bin\/ld/s/\/ld/\/ld -L\/usr\/local\/lib -R\/usr\/local\/lib/
    w
    q
__EOTEXT__
make LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/expect5.32
/usr/local/lib/libexpect5.32.a
/usr/local/lib/libexpect5.32.so
/usr/local/man/man1/expectk.1
/usr/local/man/man1/expect.1
/usr/local/man/man1/kibitz.1
/usr/local/man/man1/dislocate.1
/usr/local/man/man1/xkibitz.1
/usr/local/man/man1/tknewsbiff.1
/usr/local/man/man1/unbuffer.1
/usr/local/man/man1/mkpasswd.1
/usr/local/man/man1/passmass.1
/usr/local/man/man1/cryptdir.1
/usr/local/man/man1/decryptdir.1
/usr/local/man/man1/autoexpect.1
/usr/local/man/man3/libexpect.3
/usr/local/bin/expect
/usr/local/bin/expectk
/usr/local/bin/timed-run
/usr/local/bin/timed-read
/usr/local/bin/ftp-rfc
/usr/local/bin/autopasswd
/usr/local/bin/lpunlock
/usr/local/bin/weather
/usr/local/bin/passmass
/usr/local/bin/rftp
/usr/local/bin/kibitz
/usr/local/bin/rlogin-cwd
/usr/local/bin/xpstat
/usr/local/bin/tkpasswd
/usr/local/bin/dislocate
/usr/local/bin/xkibitz
/usr/local/bin/tknewsbiff
/usr/local/bin/unbuffer
/usr/local/bin/mkpasswd
/usr/local/bin/cryptdir
/usr/local/bin/decryptdir
/usr/local/bin/autoexpect
/usr/local/include/expect.h
/usr/local/include/expect_tcl.h
/usr/local/include/expect_comm.h
/usr/local/include/tcldbg.h
