Summary: The ical calendaring program
Name: ical
Version: 2.3.1
Release: 1
License: COPYRIGHT file
Group: Applications/Calendar
URL: http://www.annexia.org/freeware/ical/
Source: %{name}-%{version}.tar.gz
Source1: publical
Source2: ical2ics
Source3: ical-script
Source4: calicon.tcl
#Source5: calicon.png
Patch: ical-2.3.1-cc_fixes.diff
Patch1: ical-2.3.1-context_menus.diff
#Patch2: ical-2.3.1-filesel_slash_fix.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: make, vpkg-SUNWTclS
Requires: vpkg-SUNWTcl, vpkg-SUNWTk

%description
ical is a simple Tk-based calendar program for Unix machines. It was
originally written in the early 90s by Sanjay Ghemawat. Many calendar programs
have come and gone since then, but rarely have any been easier to use, faster
or better than ical.

%prep
%setup -q
%patch -p1
%patch1 -p0
#%patch2 -p0

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CXX=CC
LIBS="-L/usr/sfw/lib -R/usr/sfw/lib"
export PATH CXX LIBS

./configure
gmake

%install
mkdir -p %{buildroot}/usr/local
gmake install prefix=%{buildroot}/usr/local
mkdir -p %{buildroot}/usr/local/share/ical
cp %{SOURCE1} %{buildroot}/usr/local/share/ical/
cp %{SOURCE2} %{buildroot}/usr/local/share/ical/
cp %{SOURCE3} %{buildroot}/usr/local/bin/
cp %{SOURCE4} %{buildroot}/usr/local/share/ical/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/ical*
/usr/local/lib/ical/*/*
/usr/local/share/ical/publical
/usr/local/share/ical/ical2ics
/usr/local/share/ical/calicon.tcl
/usr/local/man/man1/ical.1
