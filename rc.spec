Summary: Rc shell from Plan 9
Name: rc
Version: 1.6
Release: 2
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
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --with-history \
  --with-readline
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING AUTHORS EXAMPLES README RELDATE ChangeLog
/usr/local/bin/rc
/usr/local/bin/-
/usr/local/bin/--
/usr/local/bin/-p
/usr/local/bin/--p
/usr/local/man/man1/rc.1
/usr/local/man/man1/history.1
