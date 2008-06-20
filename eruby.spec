%include ruby-header.spec

Summary: Embedded Ruby interpreter
Name: eruby
Version: 1.0.5
Release: 4
License: GPL
Group: Development/Libraries
URL: http://www.modruby.net/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: ruby >= %{ruby_version}
BuildRequires: ruby >= %{ruby_version}

%description
eruby interprets a Ruby code embedded text file. For example, eruby
enables you to embed a Ruby code to a HTML file.

%package static
Group: Development/Libraries
Summary: Embedded Ruby interpreter's static libraries
Requires: %{name} = %{version}
%description static
This package contains the Embedded Ruby interpreter's static libraries.
Your probably don't need them.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/ucblib -R/usr/ucblib -L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

echo "XXX %{ruby_libarchdir}"
./configure.rb
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot} mandir=%{buildroot}/usr/local/man

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/eruby
%{ruby_libarchdir}/eruby.so
/usr/local/include/eruby.h
/usr/local/man/man1/eruby.1

%files static
%defattr(-, root, bin)
/usr/local/lib/liberuby.a

%changelog
* Fri Jun 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.0.5-4
- Updated for latest version of ruby.
* Fri Aug 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.5-3
- Updated for latest version of ruby.

