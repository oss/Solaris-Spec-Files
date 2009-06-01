%define webalizer_version 2.21-02

Name:		webalizer
Version: 	2.21_02
Release:	2
Group:		Applications/Networking
License:	GPL
URL:		http://www.mrunix.net/webalizer
Source0:	ftp://ftp.mrunix.net/pub/webalizer/webalizer-%{webalizer_version}-src.tgz
Source1:	webalizer.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	db4-devel gd-devel libpng3-devel
BuildRequires:	automake autoconf

Summary:        Web server log analysis program

%description
Webalizer is a web server log file analysis program which
produces usage statistics in HTML format for viewing with
a browser.  The results are presented in both columnar and
graphical format, which facilitates interpretation.

Webalizer supports CLF (common log format) log files, as
well as Combined log formats as defined by NCSA and
others, and variations of these which it attempts to
handle intelligently. In addition, wu-ftpd xferlog
formatted logs and squid proxy logs are supported.

Note: This is built with large file support.

%prep
%setup -q -n webalizer-%{webalizer_version}

%{__sed} -i 's:-ldb:-ldb-4:g' configure.in
autoreconf

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="gcc" CFLAGS="`/bin/getconf LFS_CFLAGS`"
CPPFLAGS="-I/usr/local/include/db4 -I/usr/local/include -D__BIT_TYPES_DEFINED__ \
          -Du_int8_t=uint8_t -Du_int16_t=uint16_t  \
          -Du_int32_t=uint32_t -Du_int64_t=uint64_t"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib -R/usr/local/lib"
export PATH CC CFLAGS CPPFLAGS LDFLAGS

./configure --enable-dns --with-png=%{_includedir} --with-pnglib=%{_libdir}
gmake -j3

%install
rm -rf %{buildroot}
%{__install} -D -m 755 webalizer %{buildroot}%{_bindir}/webalizer
%{__install} -D -m 644 webalizer.1 %{buildroot}%{_mandir}/man1/webalizer.1
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/webalizer.conf
cd %{buildroot}%{_bindir}
ln -s webalizer webazolver

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README* CHANGES COPYING Copyright DNS.README INSTALL
%{_bindir}/*
%{_sysconfdir}/webalizer.conf
%{_mandir}/man1/webalizer.1

%changelog 
* Mon Jun 01 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.21_02-2
- Fixed configuration file

* Thu May 29 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.21_02-1
- Updated to version 2.21-02
- Added configuration file
- Added changelog
