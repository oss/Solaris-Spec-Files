Name: bash
Version: 2.05a
Release: 1
Summary: The Bourne-Again shell
Copyright: GPL
Group: System Environment/Shells
Source0: bash-%{version}.tar.gz
Source1: bash-doc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Bash-%{version} is an sh-compatible shell with command completion and
other improvements over sh.  It aims to be a conformant implementation
of the IEEE POSIX Shell and Utilities specification (IEEE Working Group
1003.2).

After you install this package, add an entry to /etc/shells.

%prep
%setup -q
%setup -T -D -a 1

%build
./configure --prefix=/usr/local
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/bin
make install prefix=$RPM_BUILD_ROOT/usr/local
cp $RPM_BUILD_ROOT/usr/local/bin/bash $RPM_BUILD_ROOT/bin/bash

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	    /usr/local/info/bash.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/bash.info
fi

%files
%defattr(-,root,root)
%doc doc/*txt doc/*ms doc/*ps COPYING
/bin/bash
/usr/local/bin/bash
/usr/local/bin/bashbug
/usr/local/man/man1/bash.1
/usr/local/man/man1/bashbug.1
/usr/local/info/bash.info

%changelog
* Wed Dec 19 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Removed inaccurate "Conflicts:" line, corrected permissions
