Summary: Heimdal
Name: heimdal
Version: 0.6
Release: 6
Copyright: GPL
Group: System/Authentication
Source: heimdal-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Aaron Richton <richton@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Patch0: heimdal-0.6-res_nsearch.patch
# It's unclear whether this does anything since it's #if 0'd
# however Stanford recommends it 
Patch1: heimdal-0.6-verify.patch

%description
Free Kerberos implementation.

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
Group: Development
%description devel
%{name} include files, etc.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH"

%ifarch sparc64

 mkdir sparcv9-build
 COPY=`ls | grep -v sparcv9-build`
 cp -r $COPY sparcv9-build/
 cd sparcv9-build/

 LD_LIBRARY_PATH="/usr/local/lib/sparcv9"
 LD_RUN_PATH="/usr/local/lib/sparcv9"
 LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
 CC=cc CFLAGS="-xarch=v9 -mt" CPPFLAGS="-D_REENTRANT"
 export PATH LD_LIBRARY_PATH LD_RUN_PATH LDFLAGS CC CFLAGS CPPFLAGS

 ./configure --disable-berkeley-db --disable-otp --prefix=/usr/local/ --bindir=/usr/local/bin/sparcv9 --libdir=/usr/local/lib/sparcv9 --sbindir=/usr/local/sbin/sparcv9 --libexecdir=/usr/local/libexec/sparcv9 --includedir=/usr/local/include/heimdal sparcv9-sun-solaris2.9

 make

 cd ..

%endif

LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CC=cc CFLAGS="-mt" CPPFLAGS="-D_REENTRANT"
export PATH LD_LIBRARY_PATH LD_RUN_PATH LDFLAGS CC CFLAGS CPPFLAGS
./configure --disable-berkeley-db --disable-otp --prefix=/usr/local/ --includedir=/usr/local/include/heimdal


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local

%ifarch sparc64
 cd sparcv9-build/
 make install DESTDIR=$RPM_BUILD_ROOT
 cd ..
%endif

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/info/heimdal.info
/usr/local/info/heimdal.info-1
/usr/local/info/heimdal.info-2
/usr/local/libexec/*
/usr/local/man/man1/*
/usr/local/man/man5/*
/usr/local/man/man8/*
/usr/local/sbin/*

%files devel
%defattr(-,root,root)
/usr/local/include/heimdal/*
/usr/local/lib/*.a
/usr/local/man/man3/*
%ifarch sparc64
/usr/local/lib/sparcv9/*.a
%endif
