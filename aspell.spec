Summary: aspell
Name: aspell
Version: 0.50.3
Release: 2
Copyright: GPL
Group: Applications/Spelling
Source: http://ftp.gnu.org/gnu/aspell/aspell-0.50.3.tar.gz
URL: http://aspell.net/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Spelling library

%prep
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib" \
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0" \
CPPFLAGS="-I/usr/local/include -I/usr/local/include/rpm"  \
CXXFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CC="gcc" ./configure --prefix=/usr/local


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/




