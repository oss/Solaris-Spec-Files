Name:		bonobo
Summary:	Library for compound documents in GNOME
Version: 	0.18
Release: 2
Copyright: 	GPL
Group:		System Environment/Libraries
Source: 	%{name}-%{version}.tar.gz
URL: 		http://www.gnome.org/
BuildRoot:	/var/tmp/%{name}-root
Requires:	gnome-libs
Requires:	gnome-print
Requires:	oaf
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel
BuildRequires:	oaf-devel

%description
Bonobo is a library that provides the necessary framework for GNOME
applications to deal with compound documents, i.e. those with a
spreadsheet and graphic embedded in a word-processing document.

%package devel
Summary:	Libraries and include files for the Bonobo document model
Group:		Development/Libraries
Requires:	bonobo = %{PACKAGE_VERSION}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using the Bonobo document model.

%prep
%setup

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
 CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
 --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc install

for FILE in "$RPM_BUILD_ROOT/bin/*"; do
	file "$FILE" | grep -q not\ stripped && strip $FILE
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0555, bin, bin)
/usr/local/bin/*
/usr/local/lib/*.0
/usr/local/lib/*.1
/usr/local/lib/*.sh
/usr/local/lib/*.so

%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README

%defattr (0444, bin, bin)
/usr/local/share/bonobo/html/*.hierarchy
/usr/local/share/bonobo/html/*.sgml
/usr/local/share/bonobo/html/*.signals
/usr/local/share/bonobo/html/*.txt
/usr/local/share/bonobo/html/*.types
/usr/local/share/idl/*.idl
/usr/local/lib/locale/*/LC_MESSAGES/*.mo
/usr/local/share/mime-info/*.keys
/usr/local/share/oaf/*.oafinfo



%files devel

%defattr(0555, bin, bin)
%dir /usr/local/include/bonobo
/usr/local/lib/*.a
/usr/local/lib/*.la

%defattr(0444, bin, bin)
/usr/local/include/*.h
/usr/local/include/bonobo/*.h
