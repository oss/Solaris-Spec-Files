Summary:	HicolorTheme
Name:		hicolor-icon-theme
Version:	0.10
Release:        1
Copyright:	GPL
Group:		Applications/Xfce
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
hicolor-icon-theme is the default icon theme that all icon themes 
automatically inherit from. Its role in icon themes is described 
in the specification. This page hosts the definition of this theme 
(note: it doesn't contains any icons).

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
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/local/share/*

%changelog
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.10-1
- Bump to 0.10
* Tue May 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9-1
- Initial Rutgers release
