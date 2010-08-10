Name: 		libidn
Version: 	1.19
Release:	1
Group: 		System Environment/Libraries
License:	LGPL
URL:		http://www.gnu.org/software/libidn
Source:		ftp://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	pkgconfig

Summary:	Internationalized Domain Name library

%description
GNU Libidn is a fully documented implementation of the Stringprep, 
Punycode and IDNA specifications. Libidn's purpose is to encode 
and decode internationalized domain names.

%package devel
Group:		System Environment/Libraries
Requires:	libidn = %{version}-%{release}
Requires:	pkgconfig
Summary:	Development files for libidn

%description devel
This package contains files needed for building applications that use libidn.

%prep
%setup -q

%build
%configure \
	--disable-static	\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

# Get rid of unpackaged files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir 
rm -f %{buildroot}%{_infodir}/*.png

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/libidn.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
        %{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/libidn.info
fi

%files
%defattr(-, root, root, -)
%doc README COPYING* FAQ
%doc NEWS TODO ChangeLog
%doc AUTHORS THANKS
%{_libdir}/*.so.*
%{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*

%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%changelog
* Fri Aug 06 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.19-1
- Updated to 1.19

* Thu Aug 13 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.15-1
- Updated to version 1.15
- Don't build static libraries
- Added post and preun scriplets
- Packaging modifications
- Added changelog
