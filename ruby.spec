%include ruby-header.spec

# Change ruby-header.spec when updating versions

Summary: 	the Ruby scripting language
Name: 		ruby
Version: 	%{ruby_version}
Release: 	%{ruby_release}
Group: 		Development/Languages
Copyright: 	GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	tcl tcl-tk gdbm 
BuildRequires: 	tcl tcl-tk gdbm

%description
Ruby is the interpreted scripting language for quick and
easy object-oriented programming.  It has many features to
process text files and to do system management tasks (as in
Perl).  It is simple, straight-forward, and extensible.

* Features of Ruby

  + Simple Syntax
  + *Normal* Object-Oriented features(ex. class, method calls)
  + *Advanced* Object-Oriented features(ex. Mix-in, Singleton-method)
  + Operator Overloading
  + Exception Handling
  + Iterators and Closures
  + Garbage Collection
  + Dynamic Loading of Object files(on some architecture)
  + Highly Portable(works on many UNIX machines, and on DOS,
    Windows, Mac, BeOS etc.)

 [ from the README ]

%package static
Group: Development/Languages
Summary: Ruby's static library files (the .a's)
Requires: %{name} = %{version}
%description static
This package contains Ruby's static libraries (the .a's).  You probably
don't need them.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/ucblib -R/usr/ucblib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
 ./configure --prefix=/usr/local --enable-pthread --enable-shared
mv ext/Setup ext/Setup.orig
sed 's/^#//' < ext/Setup.orig | sed 's/^option/#option/' > ext/Setup
make

%install
build_dir=`pwd`
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/share/man/man1/ruby.1
%{ruby_libdir}/*
/usr/local/lib/libruby.so*
/usr/local/bin/*

%files static
%defattr(-, root, bin)
/usr/local/lib/libruby-static.a

%changelog
* Fri Jun 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.7-2
- Added /usr/ucblib to LDFLAGS so that libucb.so.1 can be found
* Wed Jun 04 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.7-1
- Updated to version 1.8.7
* Fri Aug 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.8.6-1
- Updated to the latest version.
