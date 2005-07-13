%include ruby-header.spec

Summary: Embedded Ruby interpreter
Name: eruby
Version: 1.0.5
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.modruby.net/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: ruby = %{ruby_version}
BuildRequires: ruby = %{ruby_version}

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
echo "XXX %{ruby_libarchdir}"
./configure.rb
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

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

