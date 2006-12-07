Name: cvs
Version: 1.12.13
Copyright: GPL
Group: Development/Tools
Summary: Version control software
Release: 2
Source: cvs-%{version}.tar.bz2
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%post
echo Adding info directory...
for i in `ls /usr/local/info/`; do
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             /usr/local/info/$i &>1 > /dev/null
    fi
done


%postun
echo Rebuilding info directory...
rm /usr/local/info/dir > /dev/null
for i in `ls /usr/local/info/`; do
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             /usr/local/info/$i &> /dev/null
    fi
done


%files
%defattr(-,bin,bin)
%doc COPYING README
/usr/local/info/cvs*
/usr/local/bin/cvs*
/usr/local/bin/rcs2log
/usr/local/man/man1/cvs.1
/usr/local/man/man5/cvs.5
/usr/local/man/man8/cvsbug.8
/usr/local/share/cvs
