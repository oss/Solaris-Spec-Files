Summary: aspell
Name: aspell
Version: 0.50.3
Release: 2
Copyright: GPL
Group: Applications/Spelling
Source: http://ftp.gnu.org/gnu/aspell/aspell-0.50.3.tar.gz
Patch: aspell-assert.diff
URL: http://aspell.net/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Spelling library

%prep
%setup -q

%patch -p1

%build
LD_LIBRARY_PATH="/usr/local/lib" \
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/include/rpm"  \
CXXFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CC="g++" ./configure --prefix=/usr/local


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/




