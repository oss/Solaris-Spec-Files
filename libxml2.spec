# Note that this is NOT a relocatable package
%define ver      2.6.27
%define prefix   /usr/local
%define datadir  %{prefix}/share

Summary: Library providing XML and HTML support
Name: libxml2
Version: %ver
Release: 1
Copyright: LGPL
Group: Development/Libraries
Source: ftp://xmlsoft.org/%{name}/%{name}-%{ver}.tar.bz2
BuildRoot: %{_tmppath}/libxml2-%{PACKAGE_VERSION}-root

URL: http://xmlsoft.org/
Docdir: %{datadir}/doc

Requires: readline zlib libiconv
BuildRequires: readline-devel zlib autoconf make libiconv-devel

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

%package python
Summary: libxml2 python extensions
Group: Development/Libraries
Requires: libxml2 = %{version}

%description python
Python extensions for libxml2

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
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" CC=/opt/SUNWspro/bin/cc \
    CXX=/opt/SUNWspro/bin/CC CFLAGS='-g -xs -xO3' CXXFLAGS='-g -xs -xO3' \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
     --enable-shared --disable-static --with-zlib=/usr/local \
     --prefix=%{prefix} --with-iconv=/usr/local
gmake -j3
gmake check

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
%doc AUTHORS ChangeLog NEWS README COPYING COPYING.LIB TODO
/usr/local/man/man1/xmlcatalog.1
/usr/local/man/man1/xmllint.1
/usr/local/man/man3/*
%{prefix}/lib/lib*.so.*
%{prefix}/bin/xmllint
%{prefix}/bin/xmlcatalog

%files devel
%defattr(-, root, bin)
/usr/local/man/man1/xml2-config.1*
%doc doc/*.html doc/html
%{prefix}/lib/lib*.so
#%{prefix}/lib/*.a
%{prefix}/lib/*.sh
%{prefix}/include/*
%{prefix}/bin/xml2-config
%{prefix}/share/aclocal/*
# I'm not certain if this should be included in the distribution or not.
# jmkacz: Yes. It is for programs that build against it and use pkgconfig to
#         determine what flags were used in building it. (e.g. apt-rpm)
%{prefix}/lib/pkgconfig/libxml-2.0.pc
%{prefix}/share/doc/libxml2-python-2.6.27/TODO
%{prefix}/share/doc/libxml2-python-2.6.27/examples/*.xml
%{prefix}/share/doc/libxml2-python-2.6.27/examples/*.dtd

%files python
%defattr(-, root, bin)
%{prefix}/lib/python2.4/site-packages/
%{prefix}/share/doc/libxml2-python-2.6.27/examples/*.py
