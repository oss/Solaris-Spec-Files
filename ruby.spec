%include ruby-header.spec
%include gnome-header.spec

Summary: the Ruby scripting language
Name: ruby
Version: %{ruby_version}
Release: 3
Group: Development/Languages
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
#Requires: %{gtk_pkg}
Requires: tcl tcl-tk gdbm 
#BuildRequires: %{gtk_dev}
BuildRequires: tcl tcl-tk gdbm

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
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/man/man1/ruby.1
%{ruby_libdir}
/usr/local/bin/*
