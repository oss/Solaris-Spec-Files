Summary: Plan 9 libraries backported to Unix
Name: 9libs
Version: 1.0
Release: 3
Group: Development/Libraries
Copyright: BSD-type
Source0: 9libs-%{version}.tar.gz
Source1: sam-9libs.tar.bz2
Source2: wily-9libs.tar.bz2
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make fileutils
Provides: libframe.so.0
Provides: libXg.so
Provides: libplan9c.so
Provides: libXg.so.0
Provides: libplan9c.so.0
Provides: libframe.so

%description
This is 9libs, a package of Plan 9 compatability libraries derived
from the X11 version of Rob Pike's editor, sam.

%package devel
Summary: Headers and static libraries for 9libs
Group: Development/Libraries

%description devel
This package contains the headers, static libraries and manpages for
9libs.  You won't need it unless you are building programs with 9libs.

%package -n sam
Summary: Rob Pike's plan 9 editor
Group: Applications/Editors
Requires: 9libs = %{version}

%description -n sam
This package contains Rob Pike's "sam" editor, backported to Unix.

%package -n wily
Summary: Plan9 Acme development environment for Unix
Group: Applications/Editors
Requires: 9libs = %{version}

%description -n wily
This package contains wily, a free version of Rob Pike's acme.

%prep
%setup -q
%setup -D -T -a 1
%setup -D -T -a 2

%build
# I would ./configure this to use Sun's cc, but it only compiles with gcc.
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --enable-shared \
  --enable-static --prefix=/usr/local
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install prefix=$RPM_BUILD_ROOT/usr/local \
    INSTALL="/usr/local/gnu/bin/install"
for i in sam samterm ; do
    rm -f $RPM_BUILD_ROOT/usr/local/bin/$i
    install -m 0755 sam-9libs/$i/.libs/$i $RPM_BUILD_ROOT/usr/local/bin/$i
done

mkdir $RPM_BUILD_ROOT/usr/local/doc/sam-1.0
for i in sam.ps sam.tut se.ps ; do
    install -m 0644 $RPM_BUILD_ROOT/usr/local/doc/$i \
        $RPM_BUILD_ROOT/usr/local/doc/sam-1.0/$i
    rm -f $RPM_BUILD_ROOT/usr/local/doc/$i
done

# The regexp.h file probably conflicts with the sytem regexp.h, so
# let's be safe.
mkdir $RPM_BUILD_ROOT/usr/local/include/plan9
mv $RPM_BUILD_ROOT/usr/local/include/*.h \
   $RPM_BUILD_ROOT/usr/local/include/plan9

mv $RPM_BUILD_ROOT/usr/local/lib/9libs/include/conf9libs.h \
   $RPM_BUILD_ROOT/usr/local/include/plan9

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
/usr/local/lib/lib*.so*
/usr/local/bin/B

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*a
/usr/local/man/man3/*
/usr/local/man/man4/*
/usr/local/man/man6/*
/usr/local/include/plan9

%files -n sam
%defattr(-,bin,bin)
/usr/local/bin/sam*
/usr/local/man/man1/sam.1
/usr/local/doc/sam-1.0

%files -n wily
%defattr(-,bin,bin)
/usr/local/bin/wily
