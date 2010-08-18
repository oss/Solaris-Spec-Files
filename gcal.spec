Summary:      GNU gcal
Name:         gcal
Version:      3.6
Release:      1
License:      GPL
Group:        Applications/Productivity
URL:          http://ftp.gnu.org/gnu/gcal/
Source:       http://ftp.gnu.org/gnu/gcal/gcal-%{version}.tar.gz
# Solaris doesn't like this syntax
Patch0:       gcal-solaris-compile.patch
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: texinfo >= 4.13a-2

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
%patch0 -p1

%build
%configure --disable-silent-rules --disable-nls

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/usr/local/lib/charset.alias
rm -f $RPM_BUILD_ROOT/usr/local/share/info/dir

cd $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=%{_infodir} %{_infodir}/gcal.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=%{_infodir} \
		%{_infodir}/gcal.info
fi

%files
%defattr(-,root,root,-)
%doc BUGS README THANKS COPYING NEWS doc/*
%doc TODO
%{_infodir}/gcal*
%{_datadir}/gcal
%{_bindir}/*

%changelog
* Tue Aug 17 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 3.6-1
- Update to the latest version
