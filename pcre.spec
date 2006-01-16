Summary:	Perl Compatible Regexp Library
Name:	 	pcre
Version:	6.4
Release:	1
Copyright:	GPL
Group:		Applications/Productivity
URL:		http://www.pcre.org
Vendor:		pcre
Source0:	%{name}-%{version}.tar.gz
Patch0:		pcre-size.patch
Patch1:		pcre-publicRE.patch
BuildRoot:	/var/tmp/%{name}-root

%description
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h. The official POSIX name is
regex.h, but I didn't want to risk possible problems with existing files of
that name by distributing it that way. To use it with an existing program that
uses the POSIX API, it will have to be renamed or pointed at by a link.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
CC='cc' CXX='CC' \
CFLAGS='' CXXFLAGS='' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH \
./configure --prefix=%{buildroot}/usr/local/pcre
gmake

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/local/pcre
mkdir -p %{buildroot}/usr/local/pcre/bin
mkdir -p %{buildroot}/usr/local/pcre/include
mkdir -p %{buildroot}/usr/local/pcre/lib
mkdir -p %{buildroot}/usr/local/pcre/man/man1
mkdir -p %{buildroot}/usr/local/pcre/man/man3

gmake install
gmake test

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%dir /usr/local/pcre
/usr/local/pcre/bin/*
/usr/local/pcre/include/*
/usr/local/pcre/lib/*.so*
/usr/local/pcre/lib/*.a
/usr/local/pcre/lib/pkgconfig/*
/usr/local/pcre/man/man1/*
/usr/local/pcre/man/man3/*

%changelog
* Mon Jan 16 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to version 6.4
* Fri May 16 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Initial Rutgers RPM
