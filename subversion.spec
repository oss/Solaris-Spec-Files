# apr and apr-util are already in apache2, but
# would we want subversion to depend on apache2?
# %define apache_version 2.0.54

Summary: subversion version control system
Name: subversion
Version: 1.2.3
Release: 1
License: Apache/BSD-style
Source: %{name}-%{version}.tar.bz2
Group: Applications/Internet
Requires: neon, db4, gdbm, openssl
BuildRequires: make, neon, db4, gdbm, openssl
BuildRoot: %{_tmppath}/%{name}-root

%description
Subversion is a version control system.

%prep
%setup -q -n %{name}-%{version}
rm -rf neon/

%build
#PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
PATH=/usr/local/gnu/bin:$PATH
CC="gcc"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CPPFLAGS LDFLAGS

./autogen.sh
./configure --with-zlib -disable-nls --with-neon=/usr/local --with-ssl
# --with-apr=/usr/local/apache2-%{apache_version}/bin\
# --with-apr-util=/usr/local/apache2-%{apache_version}/bin
gmake

%install
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/local/lib/*.a
rm -f %{buildroot}/usr/local/lib/*.la
rm -f %{buildroot}/usr/local/apr/lib/*.a
rm -f %{buildroot}/usr/local/apr/lib/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/apr/include/apr-0
/usr/local/apr/lib/lib*.so*
/usr/local/apr/lib/*.exp
/usr/local/apr/build
/usr/local/apr/bin
/usr/local/lib/lib*.so*
/usr/local/include
/usr/local/bin
/usr/local/man
/usr/local/info
