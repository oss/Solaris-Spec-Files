Summary:	GSview - Ghostscript graphical interface
Name:		GSview
Version:	4.8
Release:        1
Copyright:	Aladdin Free Public Licence
Group:		Applications/Productivity
Source:		gsview-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
GSview is a graphical interface for Ghostscript under MS-Windows or 
OS/2. Ghostscript is an interpreter for the PostScript page description 
language used by laser printers. For documents following the Adobe 
PostScript Document Structuring Conventions, GSview allows selected 
pages to be viewed or printed. GSview requires  Ghostscript 7.04-9.19.

%prep
%setup -q -n gsview-%{version}

%build
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
CFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" 
export CPPFLAGS CFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

cp srcunx/unx.mak Makefile

mv Makefile Makefile.wrong

sed -e 's/ $(RPM_OPT_FLAGS)//' -e 's/prefix=/prefix=\/var\/tmp\/GSview-4.8-root/' Makefile.wrong > Makefile

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/etc/*
/usr/local/man/man1/*
/usr/local/share/doc/*

%changelog
* Mon Mar 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.8-1
- Initial Rutgers release

