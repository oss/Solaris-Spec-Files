# Note that this is NOT a relocatable package
%define ver      2.5.4
%define prefix   /usr/local
%define datadir  %{prefix}/share

Summary: Library providing XML and HTML support
Name: libxml2
Version: %ver
Release: 1
Copyright: LGPL
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2-%{ver}.tar.gz
BuildRoot: %{_tmppath}/libxml2-%{PACKAGE_VERSION}-root

URL: http://xmlsoft.org/
Docdir: %{datadir}/doc

Requires: readline
Requires: zlib
BuildRequires: readline-devel
BuildRequires: zlib
BuildRequires: autoconf

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
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}

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


%changelog
* Thu Apr 26 2001 Toshio Kuratomi <badger@prtr-13.ucsc.edu>

[2.3.7]
- Added libxml.m4 to the distribution file list
- Moved the man pages from /usr/man to /usr/share/man to conform to FHS2.0
- Moved programmer documentation into the devel package

* Thu Sep 23 1999 Daniel Veillard <daniel@veillard.com>

- corrected the spec file alpha stuff
- switched to version 1.7.1
- Added validation, XPath, nanohttp, removed memory leaks
- Renamed CHAR to xmlChar

* Wed Jun  2 1999 Daniel Veillard <daniel@veillard.com>

- Switched to version 1.1: SAX extensions, better entities support, lots of
  bug fixes.

* Sun Oct  4 1998 Daniel Veillard <daniel@veillard.com>

- Added xml-config to the package

* Thu Sep 24 1998 Michael Fulbright <msf@redhat.com>

- Built release 0.30

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
     --enable-shared --enable-static --with-zlib=/usr/local --prefix=%{prefix}
make
make check

%install
rm -rf %{buildroot}

install -d %{buildroot}%{datadir}/man/man1
install -d %{buildroot}%{datadir}/man/man4
make prefix=%{buildroot}%{prefix} mandir=%{buildroot}%{datadir}/man install
mv %{buildroot}%{datadir}/man %{buildroot}/%{prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)

%doc AUTHORS ChangeLog NEWS README COPYING COPYING.LIB TODO
/usr/local/man/man1/xmlcatalog.1
/usr/local/man/man1/xmllint.1
/usr/local/man/man3/*

%{prefix}/lib/lib*.so.*
%{prefix}/bin/xmllint

%files devel
%defattr(-, root, bin)

/usr/local/man/man1/xml2-config.1*
%doc doc/*.html doc/html

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*.sh
%{prefix}/include/*
%{prefix}/bin/xml2-config
%{prefix}/share/aclocal/*
# I'm not certain if this should be included in the distribution or not.
#%{prefix}/lib/pkgconfig/libxml-2.0.pc
