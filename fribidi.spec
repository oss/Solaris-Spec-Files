Name: fribidi
Version: 0.10.4
License: GPL
Summary: Bidirectional character support library
Release: 1
Group: Application/Libraries
Source: %{name}-%{version}.tar.gz
URL: http://fribidi.org
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development

%description
GNU FriBidi is an implementation of the Unicode Bidirectional Algorithm (bidi) and Arabic Joining/Shaping.

%description devel
%{name} include files, etc.

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/local/gnu/bin:/usr/css/bin:$PATH
CC="cc"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CPPFLAGS LDFLAGS
./configure
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm %{buildroot}/usr/local/lib/libfribidi.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, other)
/usr/local/bin/fribidi*
/usr/local/lib/libfribidi.so*

%files devel
%defattr(-, root, other)
/usr/local/include/fribidi/*.h
/usr/local/lib/libfribidi.a
/usr/local/lib/pkgconfig/fribidi.pc
