Summary: Internationalized doman name library (libidn)
Name: libidn
Version: 0.5.0
License: LGPL
Group: Application/Libraries
Release: 2
Source: ftp://alpha.gnu.org/pub/gnu/libidn/libidn-0.5.0.tar.gz
URL: http://www.gnu.org
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root

%description
The %{name} package provides the internationalized domain name libraries.

%package devel
Summary: Header files needed to compile programs against libidn.
Requires: %{name} = %{version}
Group: Application/Libraries

%description devel
The %{name}-devel package provides the header (and other) files needed to compile programs against the idn library.

%prep
%setup -q

%build
CC="/opt/SUNWspro/bin/cc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" ./configure --disable-nls
gmake

%install
gmake install DESTDIR=%{buildroot}

#%clean
#rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/lib/*
/usr/local/bin/*
/usr/local/info/libidn.info
/usr/local/man/man1/*
/usr/local/man/man3/*
/usr/local/share/emacs/site-lisp/*

%files devel
%defattr(-, root, root)
/usr/local/include/*
