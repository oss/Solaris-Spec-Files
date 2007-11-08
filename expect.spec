%define tcl_ver 8.4.16

Name: expect
Version: 5.43
Copyright: BSD-like
Group: Development/Tools
Summary: A tool for writing interactive scripts
Release: 1
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: tcl >= %{tcl_ver} tcl-tk >= %{tcl_ver}
BuildRequires: tcl-headers >= %{tcl_ver}

%description
Expect lets you write scripts to automate interactive processes.  
This version of expect was built with TCL %{tcl_ver}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix="/usr/local" \
	--enable-shared \
	--with-tclinclude="/usr/local/src/tcl-%{tcl_ver}/generic"

#ed Makefile <<__EOTEXT__
#    /\/usr\/ccs\/bin\/ld/s/\/ld/\/ld -L\/usr\/local\/lib -R\/usr\/local\/lib/
#    w
#    q
#__EOTEXT__

gmake

%install
rm -rf $RPM_BUILD_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

mkdir -p $RPM_BUILD_ROOT
gmake install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/expect*
/usr/local/lib/libexpect*.a
/usr/local/lib/libexpect*.so
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
/usr/local/man/man1/multixterm.1
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
/usr/local/bin/multixterm
/usr/local/include/expect.h
/usr/local/include/expect_tcl.h
/usr/local/include/expect_comm.h
/usr/local/include/tcldbg.h

%changelog
* Wed Nov 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.4.3
- Bump to 5.4.3
