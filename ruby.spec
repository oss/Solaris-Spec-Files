%include gnome-header.spec

Summary: the Ruby scripting language
Name: ruby
Version: 1.6.4
Release: 2
Group: Development/Languages
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: tcl tcl-tk %{gtk_pkg} gdbm
BuildRequires: tcl tcl-tk %{gtk_dev} gdbm

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

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
 CFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
 ./configure --prefix=/usr/local
mv ext/Setup ext/Setup.orig
sed 's/^#//' < ext/Setup.orig | sed 's/^option/#option/' > ext/Setup
make
make test

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/man/man1/ruby.1
/usr/local/lib/ruby/1.6
/usr/local/bin/*
