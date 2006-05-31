Name: 		gtk2-docize
Version: 	1.6
Release: 	1
Copyright: 	LGPL
Group: 		System Environment/Libraries
Source: 	gtk-doc-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Summary: 	GTK-Doc API Documentation Generator
BuildRoot: 	%{_tmppath}/gtk-doc-%{version}-root
Requires:	gtk2 >= 2.8

%description
GTK-Doc is used to document C code. It is typically used to document the 
public API of libraries, such as the GTK+ and GNOME libraries, but it 
can also be used to document application code.

Note that GTK-Doc wasn't originally intended to be a general-purpose 
documentation tool, so it can be a bit awkward to setup and use. For a 
more polished general-purpose documentation tool you may want to look at 
Doxygen. However GTK-Doc has some special code to document the signals 
and properties of GTK+ widgets and GObject classes which other tools may 
not have.

GTK-Doc allows your documentation to be written in 2 ways:

    * Embedded inside the source code in specially-formatted comments.
    * Added to the 'template' files which gtk-doc outputs after scanning 
all the header files and parsing the declarations. 

From these source code comments and template files GTK-Doc generates a 
Docbook XML (or SGML) document, which is then transformed into HTML. The 
generated HTML documentation can be browsed in an ordinary web browser 
or by using the special Devhelp API browser. 

%prep
%setup -q -n gtk-doc-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local --disable-nls --disable-rebuilds

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/share/*

%changelog
* Mon May 22 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.6-1
- Initial Rutgers release.
