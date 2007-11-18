Name: gcal
Version: 3.01
Release: 1
Copyright: GPL
Group: Applications/Productivity
Source: gcal-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU gcal
%description
From the documentation:

Gcal is a program for calculating and printing calendars.  Gcal displays
hybrid and proleptic Julian and Gregorian calendar sheets, respectively,
for one month, three months or a whole year.  It also displays eternal
holiday lists for many countries around the globe, and features a very
powerful creation of fixed date lists that can be used for reminding
purposes.  Gcal can calculate various astronomical data and times of
the Sun and the Moon for at pleasure any location, precisely enough
for most civil purposes.  Gcal supports some other calendar systems,
for example the Chinese and Japanese calendar, the Hebrew calendar and
the civil Islamic calendar, too.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="gcc" CXX="g++" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

for i in `find . -name Makefile`; do mv $i $i.wrong; sed -e 's/-lintl//g' $i.wrong > $i; rm $i.wrong; done

gmake -j3

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
cd $RPM_BUILD_ROOT
rm -f usr/local/bin/gcal-gcalltx usr/local/bin/gcal-ddiff usr/local/bin/gcal-ddiffdrv usr/local/bin/gcal-gcalltx.pl usr/local/bin/gcal-dst usr/local/bin/gcal-daily usr/local/bin/gcal-mrms usr/local/bin/gcal-wlocdrv usr/local/bin/gcal-srss usr/local/bin/gcal-moon
ln -s ../share/gcal/misc/daily/daily usr/local/bin/gcal-daily
ln -s ../share/gcal/misc/ddiff/ddiff usr/local/bin/gcal-ddiff
ln -s ../share/gcal/misc/ddiff/ddiffdrv usr/local/bin/gcal-ddiffdrv
ln -s ../share/gcal/misc/dst/dst usr/local/bin/gcal-dst
ln -s ../share/gcal/misc/gcalltx/gcalltx usr/local/bin/gcal-gcalltx
ln -s ../share/gcal/misc/gcalltx/gcalltx.pl usr/local/bin/gcal-gcalltx.pl
ln -s ../share/gcal/misc/moon/moon usr/local/bin/gcal-moon
ln -s ../share/gcal/misc/mrms/mrms usr/local/bin/gcal-mrms
ln -s ../share/gcal/misc/srss/srss usr/local/bin/gcal-srss
ln -s ../share/gcal/misc/wloc/wlocdrv usr/local/bin/gcal-wlocdrv
cd $build_dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/gcal.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/gcal.info
fi

%files
%defattr(-,bin,bin)
%doc BUGS ATTENTION ABOUT-NLS README SYMBOLS THANKS MANIFEST COPYING NEWS doc/*
%doc HISTORY TODO DISCLAIM
/usr/local/man/man1/*
/usr/local/info/gcal*
/usr/local/share/gcal
/usr/local/bin/*
#/usr/local/lib/locale/locale.alias
#/usr/local/lib/locale/*/LC_MESSAGES/gcal.mo
