Name: 		m4
Version: 	1.4.9
Release:	1
Group: 		Development/Languages
Source: 	%{name}-%{version}.tar.bz2
Copyright: 	GPL
Summary: 	The GNU version of the macro processor
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu
BuildRoot: 	/var/tmp/%{name}-root
Conflicts:	vpkg-SFWgm4

%description
From the documentation:

   `m4' is a macro processor, in the sense that it copies its input to
the output, expanding macros as it goes.  Macros are either builtin or
user-defined, and can take any number of arguments.  Besides just doing
macro expansion, `m4' has builtin functions for including named files,
running UNIX commands, doing integer arithmetic, manipulating text in
various ways, recursion, etc...  `m4' can be used either as a front-end
to a compiler, or as a macro processor in its own right.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local/gnu
make

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/share/info \
	    /usr/local/gnu/share/info/m4.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/share/info \
	    /usr/local/gnu/share/info/m4.info
fi

%files
%defattr(-,root,bin)
%doc COPYING
/usr/local/gnu/bin/m4
/usr/local/gnu/share/info/m4.info
/usr/local/gnu/share/man/man1/m4.1


%changelog
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.9-1
- Updated to 1.4.9
* Thu May 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.4-1
- Cleaned up spec file, updated to 1.4.4
