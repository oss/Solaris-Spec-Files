Summary: The lua programming language
Name: lua
Version: 5.0.2
Release: 2
License: MIT
Group: Development/Languages
Source: %{name}-%{version}.tar.gz
Patch: %{name}-%{version}.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
Requires: make, sed

%description
%{summary}

%prep
%setup -q
%patch -p1

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CC=cc
LD=ld
EXTRA_INCS="-I/usr/local/include"
export PATH CC LD EXTRA_INCS

gmake sobin

%install
mv config config.ORIG
sed -e "s/@@@INSTALL_ROOT@@@/\/var\/tmp\/lua-root/" config.ORIG > config
gmake soinstall

%clean
#rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/*
/usr/local/include/*
/usr/local/lib/*
/usr/local/man/man1/*
