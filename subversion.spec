Summary: subversion version control system
Name: subversion
Version: 1.1.0rc2
Release: 2
License: Apache/BSD-style
Source: %{name}-%{version}.tar.gz
Group: Applications/Internet
Requires: neon, db4, gdbm
BuildRequires: make, neon, db4, gdbm
BuildRoot: /var/tmp/%{name}-%{version}

%description
Subversion is a version control system.

%prep
%setup -q -n %{name}-1.1.0-rc2
rm -rf neon/

%build
#PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
PATH=/usr/local/gnu/bin:$PATH
CC="gcc"
#LD="/usr/local/gnu/bin/ld"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
#export PATH CC LD CPPFLAGS LDFLAGS
export PATH CC CPPFLAGS LDFLAGS

./autogen.sh
./configure --with-zlib -disable-nls --with-neon=/usr/local
gmake

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/*
