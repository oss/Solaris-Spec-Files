Summary:	GNOME 2's virtual-terminal emulation widget
Name:		vte
Version:	0.15.3
Release:        1
Copyright:	GPL
Group:		Applications/Xfce
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2, pkgconfig, pango, xft2, perl-module-XML-Parser
BuildRequires:	gtk2-devel, pango-devel, xft2-devel, perl-module-XML-Parser

%description
GNOME 2's virtual-terminal emulation widget.

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
PATH="/opt/SUNWspro/bin:/usr/openwin/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lintl" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/vte/*
/usr/local/libexec/*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Tue May 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.12.2-1
- Initial Rutgers release
