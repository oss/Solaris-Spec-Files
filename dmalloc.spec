Summary: 	Debug Malloc (Dmalloc)
Name: 		dmalloc
Version: 	5.4.2
Release: 	1
Copyright: 	public domain
Group: 		Development/Libraries
Source: 	http://dmalloc.com/releases/%{name}-%{version}.tgz
URL: 		http://dmalloc.com/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:       Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root

%description
The debug memory allocation or "dmalloc" library has been designed as
a drop in replacement for the system's `malloc', `realloc', `calloc',
`free' and other memory management routines while providing powerful
debugging facilities configurable at runtime.  These facilities
include such things as memory-leak tracking, fence-post write
detection, file/line number reporting, and general logging of
statistics.  It also provides support for the debugging of threaded
programs.  Releases and documentation available online. 
http://dmalloc.com/


%prep
%setup -q


%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local

%ifarch sparc64

### 64bit
CC="/opt/SUNWspro/bin/cc -xarch=v9"
CFLAGS="-g -xs -DSTDC_HEADERS"
CXX="/opt/SUNWspro/bin/CC -xarch=v9"
CXXFLAGS="-g -xs -DSTDC_HEADERS"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin$PATH"
export CC CFLAGS CXX CXXFLAGS CPPGLAGS LDFLAGS PATH
./configure --prefix=%{buildroot}/usr/local --enable-threads \
    --enable-shlib --enable-cxx --disable-nls \
    --libdir=%{buildroot}/usr/local/lib/sparcv9 \
    --bindir=%{buildroot}/usr/local/bin/sparcv9
make
make heavy
make install
make distclean

%endif

### 32bit (all builds)
CC="/opt/SUNWspro/bin/cc"
CFLAGS="-g -xs -DSTDC_HEADERS"
CXX="/opt/SUNWspro/bin/CC"
CXXFLAGS="-g -xs -DSTDC_HEADERS"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin$PATH"
export CC CFLAGS CXX CXXFLAGS CPPGLAGS LDFLAGS PATH
./configure --prefix=%{buildroot}/usr/local --enable-threads \
    --enable-shlib --enable-cxx --disable-nls
make
make heavy


%install
make install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc docs/dmalloc.info docs/dmalloc.html docs/dmalloc.texi
%doc INSTALL NEWS README
/usr/local/bin/dmalloc
/usr/local/bin/sparcv9/dmalloc
/usr/local/include/dmalloc.h
/usr/local/lib/*.so
/usr/local/lib/*.a
/usr/local/lib/sparcv9/*.so
/usr/local/lib/sparcv9/*.a


%changelog
* Mon Jun 26 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 5.4.2-1
 - Initial Package
 - Added -DSTDC_HEADERS to CFLAGS and CXXFLAGS because "the autoconf process did not correctly identify that you system uses the standard malloc library types" (http://dmalloc.com/forums/topic_show.pl?tid=124)
 - Put -xarch=v9 in CC and CXX because there is at least one line where CC is used and not CFLAGS, so it tries to link a 64bit object file as 32bit and errors out with "ld: fatal: file dmalloc.o: wrong ELF class: ELFCLASS64"