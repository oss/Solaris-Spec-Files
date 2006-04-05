Summary: The lua programming language
Name: lua
Version: 5.0.2
Release: 3
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
CC=cc
LD=ld
EXTRA_INCS="-I/usr/local/include"
export PATH CC LD EXTRA_INCS

# This awk line prints every line from the original except those starting with INSTALL_ROOT, CC, WARN, MYCFLAGS, and #MYLDFLAGS. It then watches for each of those lines individually so as to print the correct replacements for each of them.
cp config config.ORIG
awk '{if ($0 !~ /^INSTALL_ROOT=|^CC=|^WARN=|^MYCFLAGS=|^#MYLDFLAGS=|^CFLAGS=/) {print}} /^INSTALL_ROOT=/ {print "INSTALL_ROOT= $(DESTDIR)/usr/local"}; /^CC=/ {print "CC=/opt/SUNWspro/bin/cc"}; /^WARN=/ {print "WARN="}; /^MYCFLAGS=/ {print "MYCFLAGS= -xO2"}; /^#MYLDFLAGS=/ {print "MYLDFLAGS=-L/usr/local/lib -R/usr/local/lib"}; /^CFLAGS=/ {print $0 " $(MYLDFLAGS)"}' < config > config.ru
cp config.ru config

gmake
gmake so
gmake sobin

%install
gmake install DESTDIR=%{buildroot}
gmake soinstall DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/include/*
/usr/local/lib/*
/usr/local/man/man1/*
