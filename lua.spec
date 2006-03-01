Summary: The lua programming language
Name: lua
Version: 5.1
Release: 1
License: MIT
Group: Development/Languages
Source: %{name}-%{version}.tar.gz
#Patch: %{name}-%{version}.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make, sed

%description
%{summary}

%prep
%setup -q
#%patch -p1

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CC=cc
LD=ld
EXTRA_INCS="-I/usr/local/include"
export PATH CC LD EXTRA_INCS

sed -e 's/^CC= gcc/CC= cc/' src/Makefile > src/Makefile.ru.1
sed -e 's/^CFLAGS= -O2 -Wall.*/CFLAGS= -xO2 \$\(MYCFLAGS\)/' src/Makefile.ru.1 > src/Makefile.ru
cp src/Makefile src/Makefile.orig
cp src/Makefile.ru src/Makefile

gmake solaris

%install
gmake install INSTALL_TOP=%{buildroot}/usr/local

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/include/*
/usr/local/lib/*
/usr/local/man/man1/*
