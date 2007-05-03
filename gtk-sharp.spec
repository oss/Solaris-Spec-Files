Summary:	GTK Sharp
Name:		gtk-sharp
Version:	2.10.0
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	glib2 >= 2.10, gtk2, libglade, mono
BuildRequires:	glib2-devel >= 2.10, gtk2-devel, libglade-devel, mono-devel, bison

%description
gtk-sharp

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include"
CFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc"
export CPPFLAGS CFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local

#for i in `find . -name Makefile`; do cp $i $i.wrong; sed -e 's/\-W\w//g' $i.wrong > $i; rm $i.wrong; done

gmake

%install
rm -rf $RPM_BUID_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/*so*
/usr/local/lib/mono/*
/usr/local/lib/gtk-sharp-2.0/*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/lib/pkgconfig/*

%changelog
* Wed May 02 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.10.0-1
- Initial Rutgers release
