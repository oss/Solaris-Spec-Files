Summary:	GSview - Ghostscript graphical interface
Name:		GSview
Version:	4.8
Release:        3
Copyright:	Aladdin Free Public Licence
Group:		Applications/Productivity
Source0:	gsview-%{version}.tar.gz
Source1:	gsview.ini
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gs-afpl, gcc-libs

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
PATH=$PATH:/usr/sfw/bin
export CPPFLAGS CFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

cp srcunx/unx.mak Makefile

mv Makefile Makefile.wrong

sed -e 's/ $(RPM_OPT_FLAGS)//' Makefile.wrong > Makefile

make

%install
rm -rf $RPM_BUID_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}
chmod 755 $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT/etc/gsview
chmod 755 $RPM_BUILD_ROOT/etc/gsview

install -m 755 ./bin/gsview $RPM_BUILD_ROOT/usr/local/bin
install -m 755 ./srcunx/gvxhelp.txt $RPM_BUILD_ROOT/usr/local/bin
install -m 644 ./srcunx/gsview.1 $RPM_BUILD_ROOT/usr/local/man/man1/gsview.1
install -m 644 gsview.css $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/gsview.css
install -m 644 cdorder.txt $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/cdorder.txt
install -m 644 regorder.txt $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/regorder.txt
install -m 644 Readme.htm $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/Readme.htm
install -m 644 LICENCE $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/LICENCE
install -m 644 ./bin/*.htm $RPM_BUILD_ROOT/usr/local/share/doc/%{name}-%{version}/
install -m 644 ./src/printer.ini $RPM_BUILD_ROOT/etc/gsview/printer.ini
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/gsview/gsview.ini


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

