Name: tcsh
Version: 6.10
%define	ext_ver	%{version}.00
Release: 2
Group: System Environment/Shells
Summary: The Berkeley C shell, with some improvements
Source: tcsh-%{version}.tar.gz
Copyright: BSD
BuildRoot: /var/tmp/%{name}-root
Conflicts: SUNWtcsh

%description
tcsh is based on csh, but it has some improvements.  Install this if
you want to use tcsh.

After you install this package, add an entry to /etc/shells.

%prep
%setup -q -n tcsh-%{ext_ver}

%build
./configure --prefix=/usr/local
make
mv tcsh tcsh.usrlocal
make distclean
./configure --prefix=
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin $RPM_BUILD_ROOT/bin \
    $RPM_BUILD_ROOT/usr/local/man/man1
cp tcsh.usrlocal $RPM_BUILD_ROOT/usr/local/bin/tcsh
strip $RPM_BUILD_ROOT/usr/local/bin/tcsh
cp tcsh $RPM_BUILD_ROOT/bin/tcsh
cp tcsh.man $RPM_BUILD_ROOT/usr/local/man/man1/tcsh.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(555,root,other) /usr/local/bin/tcsh
%attr(555,root,other) /bin/tcsh
%attr(444,root,other) /usr/local/man/man1/tcsh.1
