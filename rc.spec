Summary: Rc shell from Plan 9
Name: rc
Version: 1.7.1
Release: 1
Group: System Environment/Shells
Copyright: BSD-type
Source: rc-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: readline
BuildRequires: readline-devel

%description
rc is a command interpreter and programming language similar to sh(1).
It is based on the AT&T Plan 9 shell of the same name.  The shell
offers a C-like syntax (much more so than the C shell), and a powerful
mechanism for manipulating variables.  It is reasonably small and
reasonably fast, especially when compared to contemporary shells.  Its
use is intended to be interactive, but the language lends itself well
to scripts.

  [from the man page]

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --with-history --with-readline --prefix=/usr/local

gmake

%install
slide rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
slide gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
slide rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING AUTHORS EXAMPLES README RELDATE ChangeLog
/usr/local/bin/rc
/usr/local/man/man1/rc.1
/usr/local/man/man1/history.1
