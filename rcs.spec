Name: rcs
Version: 5.7
Copyright: GPL
Group: Development/Tools
Summary: Revision Control System
Release: 2
Source: rcs-5.7.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
From the documentation:

RCS, the Revision Control System, manages multiple revisions of files.
RCS can store, retrieve, log, identify, and merge revisions.  It is
useful for files that are revised frequently, e.g. programs,
documentation, graphics, and papers.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING CREDITS NEWS REFS
/usr/local/man/man1/ci.1
/usr/local/man/man1/co.1
/usr/local/man/man1/ident.1
/usr/local/man/man1/merge.1
/usr/local/man/man1/rcs.1
/usr/local/man/man1/rcsclean.1
/usr/local/man/man1/rcsdiff.1
/usr/local/man/man1/rcsintro.1
/usr/local/man/man1/rcsmerge.1
/usr/local/man/man1/rlog.1
/usr/local/man/man5/rcsfile.5
/usr/local/bin/ci
/usr/local/bin/co
/usr/local/bin/ident
/usr/local/bin/merge
/usr/local/bin/rcs
/usr/local/bin/rcsclean
/usr/local/bin/rcsdiff
/usr/local/bin/rcsmerge
/usr/local/bin/rlog
