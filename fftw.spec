Name:           fftw
Version:        3.2
Release:        1
Summary:        Fast Fourier Transform library
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.fftw.org/
Source0:        ftp://ftp.fftw.org/pub/fftw/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires(post): %{_bindir}/install-info
Requires(preun): %{_bindir}/install-info

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.


%package        devel
Summary:        Headers, libraries and docs for the FFTW library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release} pkgconfig


%description    devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library.


%package        static
Summary:        Static version of the FFTW library
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The fftw-static package contains the statically linkable version of
the FFTW fast Fourier transform library.


%prep
%setup -q -c %{name}-%{version}
mv %{name}-%{version} single
cp -a single double
cp -a single long


%build
PATH="/opt/SUNWspro/bin:${PATH}"
CC="cc" CXX="CC" F77="f77"
CPPFLAGS="-I/opt/SUNWspro/include -I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/opt/SUNWspro/lib -R/opt/SUNWspro/lib \
		-L/usr/local/lib -R/usr/local/lib"
LIBS="-lsunmath"
export PATH CC CXX F77 CPPFLAGS LD LDFLAGS LIBS

CONFIG_FLAGS="--prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} \
		--enable-shared --enable-threads --disable-dependency-tracking"
cd double
	./configure $CONFIG_FLAGS
	gmake -j3
cd ..
cd single
	./configure $CONFIG_FLAGS --enable-single
	gmake -j3
cd ..
cd long
	./configure $CONFIG_FLAGS --enable-long-double
	gmake -j3
cd ..


%install
rm -rf ${RPM_BUILD_ROOT}
cd double
	gmake install DESTDIR=${RPM_BUILD_ROOT}
	cp -a AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO ../
	cp -a doc/ ../
cd ..
cd single
	gmake install DESTDIR=${RPM_BUILD_ROOT}
cd ..
cd long
	gmake install DESTDIR=${RPM_BUILD_ROOT}
cd ..
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%post devel
%{_bindir}/install-info --section="Math" %{_infodir}/%{name}.info.gz %{_infodir}/dir  2>/dev/null || :

%preun devel
if [ "$1" = 0 ]; then
  %{_bindir}/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/*.pdf doc/html/* doc/FAQ/fftw-faq.html/
%doc %{_infodir}/*.info*
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%files static
%defattr(-,root,root,-)
%exclude %{_libdir}/*.la
%{_libdir}/*.a


%changelog
* Wed Jan 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.2-1
- Initial RU-Solaris build

