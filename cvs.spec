Name: cvs
Version: 1.11.1p1
Copyright: GPL
Group: Development/Tools
Summary: Version control software
Release: 1
Source: http://ftp.cvshome.org/cvs-1.11.1/cvs-1.11.1p1.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description

CVS is a version control system, which allows you to keep old versions
of files (usually source code), keep a log of who, when, and why
changes occurred, etc., like RCS or SCCS.  It handles multiple
developers, multiple directories, triggers to enable/log/control
various operations, and can work over a wide area network.  The
following tasks are not included; they can be done in conjunction with
CVS but will tend to require some script-writing and software other
than CVS: bug-tracking, build management (that is, make and make-like
tools), and automated testing.

   [from README]

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/cvs.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/cvsclient.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/cvs.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/cvsclient.info
fi

%files
%defattr(-,bin,bin)
%doc COPYING README
/usr/local/info/*
/usr/local/bin/*
/usr/local/man/man1/cvs.1
/usr/local/man/man5/cvs.5
/usr/local/man/man8/cvsbug.8
/usr/local/lib/cvs
