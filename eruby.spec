%include ruby-header.spec

Summary: Embedded Ruby interpreter
Name: eruby
Version: 0.9.6
Release: 2
License: GPL
Group: Development/Libraries
URL: http://www.modruby.net/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: ruby = 1.6.8
BuildRequires: ruby = 1.6.8

%description
eruby interprets a Ruby code embedded text file. For example, eruby
enables you to embed a Ruby code to a HTML file.

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
/usr/local/lib/liberuby.a
%{ruby_libarchdir}/eruby.so
/usr/local/include/eruby.h
/usr/local/man/man1/eruby.1
