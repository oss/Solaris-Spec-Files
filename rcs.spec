Summary: Revision Control System
Name: rcs
Version: 5.7
Release: 3
Copyright: GPL
Group: Development/Tools
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: diffutils
Requires: diffutils

%description
From the documentation:

RCS, the Revision Control System, manages multiple revisions of files.
RCS can store, retrieve, log, identify, and merge revisions.  It is
useful for files that are revised frequently, e.g. programs,
documentation, graphics, and papers.

%prep
%setup -q

%build
PATH="/usr/local/gnu/bin:$PATH" DIFF="/usr/local/gnu/bin/diff" \
  ./configure --prefix=/usr/local --with-diffutils
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}/usr/local

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc COPYING CREDITS NEWS REFS rcs.ms rcs_func.ms
/usr/local/man/man*/*
/usr/local/bin/*
