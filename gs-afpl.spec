Name: gs-afpl
Version: 8.53
Copyright: Freely available
Group: Applications/Publishing
Summary: AFPL Ghostscript
Release: 1
Source0: ghostscript-%{version}.tar.bz2
Source1: ghostscript-fonts-std-8.11.tar.gz
Source2: ghostscript-fonts-other-6.0.tar.gz
Patch:   gs-sun.patch
Requires: gs-fonts
BuildRoot: %{_tmppath}/%{name}-root
Requires: libpng3 zlib libjpeg
BuildRequires: libpng3-devel zlib-devel %{requires}
Conflicts: vpkg-SFWgs
Provides: ghostscript

%description 
Aladdin Ghostscript lets you print or view postscript files without a
postscript printer.  You need to install gs-fonts if you want to use
Ghostscript.

%package fonts
Summary: Ghostscript fonts
Group: Applications/Publishing

%description fonts
Gs-fonts contains the fonts used by Ghostscript.  

%prep
%setup -q -n ghostscript-%{version}
%setup -q -D -T -a 1 -n ghostscript-%{version}	
%setup -q -D -T -a 2 -n ghostscript-%{version}
# The patch fixes stdint_.h so it works on a Sun Solaris machine
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls --without-jbig2dec

# Why this program bothers with autoconf boggles the mind.

make \
CFLAGS='-O -I/usr/local/include' \
XLDFLAGS='-L/usr/local/lib -R/usr/local/lib'

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local
tar cf - fonts | (cd $RPM_BUILD_ROOT/usr/local/share/ghostscript && tar xf -)

%post
cat<<EOF
FYI, ghostscript includes dvipdf which needs teTeX, but the package
is set up not to require teTeX.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/man/de/man1/*
/usr/local/share/ghostscript/%{version}

%files fonts
%defattr(-,root,root)
/usr/local/share/ghostscript/fonts/*

%changelog
* Fri Mar 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.53-1
- First Rutgers release of AFPL Ghostscript 8.53
* Wed Feb 08 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 8.50-1
- Updated to the latest version.
