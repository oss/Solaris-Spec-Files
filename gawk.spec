Name: 		gawk
Version:	3.1.7
Release:	1
Group:		System Environment/Base
License:	GPL
URL:		http://www.gnu.org/software/gawk
Source:		ftp://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:	The GNU awk implementation

%description
The awk programming language is a text processing language designed by Alfred V. Aho, Peter J. Weinberger, 
and Brian W. Kernighan. 

The GNU implementation of awk is called gawk; it is fully compatible with the System V Release 4 version of awk. 
gawk is also compatible with the POSIX specification of the awk language. This means that all properly written 
awk programs should work with gawk.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS 

./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} --disable-nls

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
cd %{buildroot}/usr/local
unhardlinkify.py %{buildroot}

rm -f %{buildroot}%{_infodir}/dir

%{_bindir}/unhardlinkify.py %{buildroot}

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/gawk.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
	%{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/gawk.info
fi

%files
%defattr(-, root, root)
%doc README README_d/README.solaris 
%doc POSIX.STD COPYING AUTHORS ChangeLog
%doc NEWS FUTURES PROBLEMS LIMITATIONS 
%doc doc/*.eps doc/awkforai.txt
%{_bindir}/*
%{_datadir}/awk/
%{_infodir}/*.info
%{_mandir}/man1/*
%{_libexecdir}/awk/

%changelog
* Wed Aug 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.1.7-1
- Updated to version 3.1.7

* Sun Nov 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.1.6
- Naveen stop building with gcc!!! :-p

* Tue Aug 14 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 3.1.5
- Updated to 3.1.5
