Name: tla
Summary: A distributed revision control system 
Version: 1.3.3
Release: 1
License: GPL
Group: Development/Tools
Source: ftp://ftp.gnu.org/gnu/gnu-arch/tla-%{version}.tar.gz
URL: http://www.gnu.org/software/gnu-arch
#BuildRequires: gmake

BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
GNU arch is a revision control system which serves a similiar
purpose to CVS.  However, GNU arch is far more powerful
than CVS; it is fully distributed, has atomic changesets that
support file renames, and supports repeated merging. 

%prep
%setup -q

%build

mkdir +build
cd +build
../src/configure --prefix=/usr/local --config-shell /bin/bash --destdir=%{buildroot} --with-posix-shell=/bin/bash --with-cc=gcc --with-gnu-tar=/usr/local/gnu/bin

gmake 

%install
rm -rf %{buildroot}
cd +build
gmake install

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc COPYING
%{_bindir}/tla
