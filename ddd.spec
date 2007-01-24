# Note that this is NOT a relocatable package
%define name     ddd
%define ver      3.3.11
%define rel      1

Name: %name
Summary: graphical debugger front-end; GDB, DBX, Ladebug, JDB, Perl, Python
Version: %ver
Release: %rel
Copyright: GPL
Group: Development/Debuggers
Source: ftp://ftp.gnu.org/gnu/ddd/%{name}-%{ver}.tar.gz
URL: http://www.gnu.org/software/ddd/
Requires: texinfo info xpm readline5 gdb
BuildRequires: texinfo info xpm readline-devel readline5 gdb
BuildRoot: /var/tmp/%{name}-root

%description
DDD is a graphical front-end for command-line debuggers such as GDB,
DBX, WDB, Ladebug, JDB, XDB, the Perl debugger, or the Python
debugger.  Besides "usual" front-end features such as viewing source
texts, DDD has become famous through its interactive graphical data
display, where data structures are displayed as graphs.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ncursesw" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-readline --enable-builtin-manual --enable-builtin-news --enable-builtin-license
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info %{_prefix}/info/ddd.info* %{_prefix}/info/dir
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
   /usr/local/bin/install-info --delete %{_prefix}/info/ddd.info* %{_prefix}/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ANNOUNCE BUGS COPYING COPYING.LIB CREDITS NEWS NICKNAMES OPENBUGS
%doc PROBLEMS README TIPS TODO
%doc doc/ddd-paper.ps doc/ddd.pdf doc/ddd.ps         
%{_prefix}/bin/ddd
%{_prefix}/man/man1/ddd.1*
%{_prefix}/info/ddd.info*
%{_prefix}/info/ddd-themes.info*
%{_prefix}/share/%{name}-%{ver}/vsllib/*
%{_prefix}/share/%{name}-%{ver}/themes/*
%{_prefix}/share/%{name}-%{ver}/ddd/Ddd
%{_prefix}/share/%{name}-%{ver}/COPYING
%{_prefix}/share/%{name}-%{ver}/NEWS
