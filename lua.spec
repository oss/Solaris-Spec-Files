Summary: The lua programming language
Name: lua
Version: 5.1
Release: 2
License: MIT
Group: Development/Languages
Source: %{name}-%{version}.tar.gz
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make

%description
%{summary}

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CC=/opt/SUNWspro/bin/cc
LD=/usr/ccs/bin/ld
export PATH CC LD

cp Makefile Makefile.orig
sed -e 's/^\(INSTALL_TOP= \)\(.*\)$/\1\$(DESTDIR)\2/' Makefile > Makefile.ru.2
sed -e 's/^#\(INSTALL_EXEC= \)\(.*\)$/\1\2/' Makefile.ru.2 > Makefile.ru.1
sed -e ' s/^#\(INSTALL_DATA= \)\(.*\)$/\1\2/' Makefile.ru.1 > Makefile.ru
cp Makefile.ru Makefile

cp src/Makefile src/Makefile.orig
awk '{if ($0 ~ /^CC= gcc$/) {print "CC= /opt/SUNWspro/bin/cc"} else {if ($0 ~ /^CFLAGS=.*$/) {print "CFLAGS= -xO2 -I/usr/local/include $(MYCFLAGS)"} else {print}}}' < src/Makefile > src/Makefile.ru
cp src/Makefile.ru src/Makefile

gmake solaris CC="$CC" LD="$LD"

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/include/*
/usr/local/lib/*
/usr/local/man/man1/*
