Summary: Simplified Wrapper and Interface Generator
Name: swig
Version: 1.3.13
Release: 0ru
Group: Applications/Internet
Copyright: Unknown
Source: http://telia.dl.sourceforge.net/sourceforge/swig/swig-1.3.13.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
SWIG is a software development tool that connects programs written
in C and C++ with a variety of high-level programming languages. SWIG
is primarily used with common scripting languages such as Perl, Python,
Tcl/Tk, Ruby, Guile and MzScheme, however the list of supported
languages also includes non-scripting languages such as Java and Eiffel.
SWIG is most commonly used to create high-level interpreted programming
environments and as a tool for building user interfaces.


%prep
%setup -q -n SWIG-1.3.13

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" 

CC="cc" ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/bin/swig
/usr/local/lib/swig1.3/*
/usr/local/lib/libswig*