# Note that this is NOT a relocatable package
%define name     ddd
%define ver      3.3.1
%define rel      2

Name: %name
Summary: graphical debugger front-end; GDB, DBX, Ladebug, JDB, Perl, Python
Version: %ver
Release: %rel
Copyright: GPL
Group: Development/Debuggers
Source: ftp://ftp.gnu.org/gnu/ddd/%{name}-%{ver}.tar.gz
URL: http://www.gnu.org/software/ddd/
Requires: texinfo info xpm readline gdb
BuildRequires: texinfo info xpm readline-devel readline gdb
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
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 ./configure
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} install

( cd $RPM_BUILD_ROOT
  for dir in .%{_prefix}/bin
  do
    [ -d $dir ] || continue
    strip $dir/* || :
  done
  gzip -9nf .%{_prefix}/info/ddd.info*
# bzip2 -9z .%{_prefix}/info/ddd.info*
  rm -f .%{_prefix}/info/dir
)

%post
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info %{_prefix}/info/ddd.info.* %{_prefix}/info/dir
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
   /usr/local/bin/install-info --delete %{_prefix}/info/ddd.info.* %{_prefix}/info/dir
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
%{_prefix}/share/%{name}-%{ver}/vsllib/*
%{_prefix}/share/%{name}-%{ver}/themes/*
%{_prefix}/share/%{name}-%{ver}/ddd/Ddd
