Name: gs
Version: 8.71
License: Freely available
Group: Applications/Publishing
Summary: AFPL Ghostscript
Release: 1
Source0: ghostscript-%{version}.tar.gz
Source1: ghostscript-fonts-std-8.11.tar.gz
Source2: ghostscript-fonts-other-6.0.tar.gz
Patch0:	gs-gsnogc.patch
Patch1:   gs-sun.patch
Patch2:	gs-voidreturn.patch
Requires: gs-fonts
BuildRoot: %{_tmppath}/%{name}-root
Requires: libpng3 zlib libjpeg
BuildRequires: libpng3-devel zlib-devel %{requires} sed
Conflicts: vpkg-SFWgs
Obsoletes: gs-afpl
Provides: ghostscript gs-afpl

%define _mandir /usr/local/man

%description 
Aladdin Ghostscript lets you print or view postscript files without a
postscript printer.  You need to install gs-fonts if you want to use
Ghostscript.

%package fonts
Summary: Ghostscript fonts
Group: Applications/Publishing

%description fonts
Gs-fonts contains the fonts used by Ghostscript.  

%package devel
Summary: Files for developing applications that use ghostscript
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
The header files for developing applications that use ghostsript.

%prep
%setup -q -n ghostscript-%{version}
%setup -q -D -T -a 1 -n ghostscript-%{version}	
%setup -q -D -T -a 2 -n ghostscript-%{version}

%patch0 -p0
# The patch fixes stdint_.h so it works on a Sun Solaris machine
%patch1 -p0
%patch2 -p0

# manually replacing fast ints
find . -type f -exec grep -l int_fast {} \; | xargs -I{} /usr/local/bin/sed --in-place=RUTGERS s/int_fast/int/g {}
find . -type f -exec grep -l INT_FAST {} \; | xargs -I{} /usr/local/bin/sed --in-place=RUTGERS s/INT_FAST/INT/g {}

%build
PATH="/opt/SUNWspro/bin:/usr/sfw/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --with-ijs --prefix=/usr/local --disable-nls --without-jbig2dec

# Build IJS
cd ijs
./autogen.sh
./configure --enable-shared
make
cd ..

#mv Makefile Makefile.wrong
#mv src/unix-dll.mak src/unix-dll.mak.wrong

#sed -e 's/-fPIC/-KPIC/g' Makefile.wrong > Makefile
#sed -e 's/-shared -Wl,-soname=/-Bdynamic -G -h/' src/unix-dll.mak.wrong > src/unix-dll.mak

# Why this program bothers with autoconf boggles the mind.

gmake \
XLDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
FONTCONFIG_LIBS='-L/usr/local/lib -R/usr/local/lib -lfontconfig' \
XLDFLAGS='-L/usr/openwin/lib -R/usr/openwin/lib' \
EXTRALIBS='-ldl -lm -L/usr/local/lib -lfontconfig -R/usr/local/lib' \
XLIBDIRS='-L/usr/openwin/lib -R/usr/openwin/lib' \
CAIRO_LIBS='-L/usr/local/lib -R/usr/local/lib -lcairo'

gmake soclean

# FIXME: LDFLAGS_SO should specify a -h option to set a soname for the lib AND NOT THE BINARIES,
# but that's more complex than we'll tackle today.
gmake so \
LDFLAGS_SO='-Wl,-G' \
XLDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
FONTCONFIG_LIBS='-L/usr/local/lib -R/usr/local/lib -lfontconfig' \
XLDFLAGS='-L/usr/openwin/lib -R/usr/openwin/lib' \
EXTRALIBS='-ldl -lm -L/usr/local/lib -lfontconfig -R/usr/local/lib' \
XLIBDIRS='-L/usr/openwin/lib -R/usr/openwin/lib' \
CAIRO_LIBS='-L/usr/local/lib -R/usr/local/lib -lcairo'

%install
rm -rf $RPM_BUILD_ROOT
gmake install prefix=$RPM_BUILD_ROOT/usr/local
gmake soinstall prefix=$RPM_BUILD_ROOT/usr/local
tar cf - fonts | (cd $RPM_BUILD_ROOT/usr/local/share/ghostscript && tar xf -)
gmake install soinstall \
%{?_with_freetype:FT_BRIDGE=1} \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	gsincludedir=$RPM_BUILD_ROOT%{_includedir}/ghostscript/ \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	gsdir=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	gsdatadir=$RPM_BUILD_ROOT%{_datadir}/%{name}/%{version} \
	gssharedir=$RPM_BUILD_ROOT%{_libdir}/%{name}/%{version} 

mv -f $RPM_BUILD_ROOT%{_bindir}/gsc $RPM_BUILD_ROOT%{_bindir}/gs

cd ijs
gmake install prefix=$RPM_BUILD_ROOT/usr/local
cd ..

#Header files.
mkdir -p $RPM_BUILD_ROOT%{_includedir}/ghostscript
#install is not working on Solaris (https://support.process-one.net/browse/EJAB-649), and there is no ginstall, so doing it manually
#install -m0644 base/errors.h $RPM_BUILD_ROOT%{_includedir}/ghostscript
cp base/errors.h $RPM_BUILD_ROOT%{_includedir}/ghostscript
chmod 755 $RPM_BUILD_ROOT%{_includedir}/ghostscript
chmod 644 $RPM_BUILD_ROOT%{_includedir}/ghostscript/*

#Don't ship libtool la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/libijs.la

# Keep the /usr/local/man man pages, rm the /usr/local/share man pages
rm -R $RPM_BUILD_ROOT/usr/local/share/man

# Also rm non-English man pages
rm -R $RPM_BUILD_ROOT/usr/local/man/de/

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
/usr/local/lib/*
%{_mandir}/man1/*
/usr/local/share/ghostscript/%{version}
/usr/local/share/%{name}/%{version}/*
/usr/local/lib/libgs.so
/usr/local/lib/libijs.so

%files fonts
%defattr(-,root,root)
/usr/local/share/ghostscript/fonts/*

# FIXME: /usr/local/lib/libgs.a should be in gs-devel, oh well
%files devel
%defattr(-,root,root)
%dir %{_includedir}/ghostscript
%{_includedir}/ghostscript/*.h
%dir %{_includedir}/ijs
%{_includedir}/ijs/*
%{_bindir}/ijs-config
%{_libdir}/libijs.a

%changelog
* Thu Aug 18 2011 Phillip Quiza <pquiza@nbcs.rutgers.edu> 8.71-1
- Updated to 8.71
- Included support for gs-devel
* Wed Apr 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.53-3
- Fixed gcc-libs dependency
* Tue Mar 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.53-2
- Changed to GCC because we now use shared libraries on this package
* Fri Mar 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.53-1
- First Rutgers release of AFPL Ghostscript 8.53
* Wed Feb 08 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 8.50-1
- Updated to the latest version.
