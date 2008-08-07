Name: elinks
Summary: A text-mode Web browser.
Version: 0.11.4
Release: 1
Source: http://elinks.or.cz/download/elinks-%{version}.tar.bz2
Patch0: elinks-0.11.4-rdynamic.patch
Patch1: elinks-0.11.4-session.patch
Patch2: elinks-0.11.4-conv.patch
Group: Applications/Internet
URL: http://elinks.or.cz/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: libidn
Requires: expat
Requires: bzip2
Requires: openssl
Requires: zlib
BuildRequires: pkgconfig
BuildRequires: openssl
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: libidn-devel
BuildRequires: autoconf
BuildRequires: zlib
BuildRequires: heimdal heimdal-devel heimdal-lib
BuildRequires: cyrus-sasl
License: GPL
Provides: webclient
Obsoletes: links
Provides: links

%description
Links is a text-based Web browser. Links does not display any images,
but it does support frames, tables and most other HTML tags. Links'
advantage over graphical browsers is its speed--Links starts and exits
quickly and swiftly displays Web pages.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
cd src/session
%patch1 -p0
cd ../../
cd src/util
%patch2 -p0
cd ../../

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS 

./configure \
   --disable-nls \
   --without-x \
   --with-gssapi \
   --disable-smb \
   --with-openssl=/usr/local/ssl

gmake

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
cp %{buildroot}/usr/local/bin/elinks %{buildroot}/usr/local/bin/links

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README SITES TODO
/usr/local/bin/links
/usr/local/bin/elinks
/usr/local/man/man1/elinks.1
/usr/local/man/man5/elinks.conf.5
/usr/local/man/man5/elinkskeys.5

%changelog
* Thu Aug 7 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.11.4-1
- patched to compile on sun cc
- first solaris release
