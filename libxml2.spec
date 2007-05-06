# Note that this is NOT a relocatable package
%define name	libxml2
%define version	2.6.28
%define prefix	/usr/local
%define datadir	%{prefix}/share
%define release	2

Summary:	Library providing XML and HTML support
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Development/Libraries
Source:		ftp://xmlsoft.org/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/libxml2-%{version}-%{release}-root
URL:		http://xmlsoft.org/
Requires:	readline zlib libiconv
BuildRequires:	readline-devel zlib pkgconfig
BuildRequires:	autoconf make libiconv-devel

%description
This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary:	Libraries, includes, etc. to develop XML and HTML applications
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package python
Summary:	libxml2 python extensions
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description python
Python extensions for libxml2

%prep
%setup -q

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-g -xs"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--disable-static \
	--with-zlib="/usr/local" \
	--prefix=%{prefix} \
	--with-iconv="/usr/local"

gmake %{?_smp_mflags}
#gmake check

%install
rm -rf %{buildroot}

install -d %{buildroot}%{datadir}/man/man1
install -d %{buildroot}%{datadir}/man/man4

gmake prefix=%{buildroot}%{prefix} mandir=%{buildroot}%{datadir}/man install
mv %{buildroot}%{datadir}/man %{buildroot}/%{prefix}
rm %{buildroot}/usr/local/lib/libxml2.la
rm %{buildroot}/usr/local/lib/python2.4/site-packages/libxml2mod.la
rm -rf %{buildroot}/usr/local/share/gtk-doc/html/libxml2
# If you want a libxml2-python package, then package these files instead
# of deleting them (and [Build]Requires: python)
#rm -rf %{buildroot}/usr/local/lib/python2.4
#rm -rf %{buildroot}/usr/local/share/doc/libxml2-python-2.6.22

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc Copyright AUTHORS ChangeLog NEWS README COPYING TODO
/usr/local/man/man1/xmlcatalog.1
/usr/local/man/man1/xmllint.1
/usr/local/man/man3/*
%{prefix}/lib/lib*.so.*
%{prefix}/bin/xmllint
%{prefix}/bin/xmlcatalog

%files devel
%defattr(-, root, bin)
/usr/local/man/man1/xml2-config.1*
%{prefix}/lib/lib*.so
#%{prefix}/lib/*.a
%{prefix}/lib/*.sh
%{prefix}/include/*
%{prefix}/bin/xml2-config
%{prefix}/lib/pkgconfig/libxml-2.0.pc
%{prefix}/share/aclocal/
%{prefix}/share/doc/%{name}-%{version}/

%files python
%defattr(-, root, bin)
%{prefix}/lib/python2.4/site-packages/
%{prefix}/share/doc/%{name}-python-%{version}/

%changelog
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.6.28-2
- Respin.
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.6.28-1
- Version Bump.


