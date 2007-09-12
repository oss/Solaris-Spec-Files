%define name webalizer
%define version 2.01_10
%define release 3
%define prefix /usr/local

Summary: Web server log analysis program.

Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Networking
Copyright: GPL
Source0: webalizer-2.01-10-src.tar.bz2
BuildRoot: /var/local/tmp/%{name}-root
requires: gd >= 1.8.4 libpng3

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
%setup -q -n webalizer-2.01-10

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="gcc"  # I hate it as much as you do, but gcc is a must
CFLAGS="`/bin/getconf LFS_CFLAGS`"
CPPFLAGS="-I/usr/sfw/include -I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib -R/usr/local/lib"
export PATH CC CFLAGS CPPFLAGS LDFLAGS

./configure --enable-dns --with-dblib=%{prefix}/lib \
%ifos solaris2.9
--with-png=/usr/sfw/lib
%else
--with-png=%{prefix}/lib
%endif

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man1
mkdir -p $RPM_BUILD_ROOT%{prefix}/etc
install -m 755 webalizer $RPM_BUILD_ROOT%{prefix}/bin
install -m 644 webalizer.1 $RPM_BUILD_ROOT%{prefix}/man/man1
install -m 644 sample.conf $RPM_BUILD_ROOT%{prefix}/etc/webalizer.conf.rpm
cd $RPM_BUILD_ROOT%{prefix}/bin
ln -s webalizer webazolver

%post
cat << EOF

Copy /usr/local/etc/webalizer.conf.rpm to /usr/local/etc/webalizer.conf
in order to use webalizer!

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc CHANGES COPYING Copyright DNS.README INSTALL README README.FIRST msfree.png webalizer.png
%{prefix}/bin/*
%{prefix}/etc/webalizer.conf.rpm
%{prefix}/man/man*/*
