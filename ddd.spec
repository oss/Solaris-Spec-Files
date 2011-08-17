# Note that this is NOT a relocatable package
%define name     ddd
%define ver      3.3.12
%define rel      1

Name: %name
Summary: graphical debugger front-end; GDB, DBX, Ladebug, JDB, Perl, Python
Version: %ver
Release: %rel
License: GPL
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
%configure --with-readline --enable-builtin-manual --enable-builtin-news --enable-builtin-license
gmake

%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/local/share/info/dir

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
%doc COPYING CREDITS NEWS
%doc PROBLEMS README TIPS TODO
%doc doc/ddd-paper.ps doc/ddd.pdf doc/ddd.ps         
/usr/local/share/info/*
/usr/local/share/man/man1/*
/usr/local/share/applications/*
%{_prefix}/bin/ddd
%{_prefix}/share/%{name}-%{ver}/vsllib/*
%{_prefix}/share/%{name}-%{ver}/themes/*
%{_prefix}/share/%{name}-%{ver}/ddd/Ddd
%{_prefix}/share/%{name}-%{ver}/COPYING
%{_prefix}/share/%{name}-%{ver}/NEWS

%changelog
* Mon Aug 09 2010 Steven Lu <sjlu@nbcs.rutgers.edu> - 3.3.12-1
- bump, spec file update
