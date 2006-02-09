Name: gs
Version: 8.50
Copyright: GPL
Group: Applications/Publishing
Summary: GPL Ghostscript
Release: 1
Source0: ghostscript-%{version}-gpl.tar.gz
Source1: ghostscript-fonts-std-8.11.tar.gz
Source2: ghostscript-fonts-other-6.0.tar.gz
Patch:   gs-sun.patch
Requires: gs-fonts
BuildRoot: %{_tmppath}/%{name}-root
Requires: libpng3 zlib libjpeg62
BuildRequires: libpng3-devel zlib-devel libjpeg62-devel %{requires}
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
%setup -q -n ghostscript-%{version}-gpl
%setup -q -D -T -a 1 -n ghostscript-%{version}-gpl
%setup -q -D -T -a 2 -n ghostscript-%{version}-gpl
# The patch fixes stdint_.h so it works on a Sun Solaris machine
%patch -p1

%build
PATH=/usr/local/gnu/bin:/usr/local/bin:/opt/SUNWspro/bin:$PATH
export PATH
CC=cc \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/include' \
./configure --without-jbig2dec

# Why this program bothers with autoconf boggles the mind.

make \
CFLAGS='-O -I/usr/local/include' \
XLDFLAGS='-L/usr/local/lib -R/usr/local/lib'

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}/usr/local
tar cf - fonts | (cd %{buildroot}/usr/local/share/ghostscript && tar xf -)

%post
cat<<EOF
FYI, ghostscript includes dvipdf which needs teTeX, but the package
is set up not to require teTeX.
EOF

%clean
rm -rf %{buildroot}

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
* Wed Feb 08 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 8.50-1
- Updated to the latest version.