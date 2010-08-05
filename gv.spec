Name: gv
Version: 3.7.1
Release: 1
Summary: The gv PostScript viewer
Group: Applications/Productivity
License: GPL
URL: http://ftp.gnu.org/gnu/gv/
Source: %{name}-%{version}.tar.gz
Requires: Xaw3d >= 1.5
BuildRoot: /var/local/tmp/%{name}-root/

%description
Gv is a PostScript viewer based on Ghostview.

%prep
%setup -q

# Solaris 9 does not have strtold()
sed -i 's|strtold|strtod|' src/secscanf.c

%build
%configure  --enable-setenv-code
gmake -j3

%install
gmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_infodir}/dir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/gv*
%{_datadir}/gv/
%{_infodir}/gv.info
%{_mandir}/man1/*.1

%changelog
* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 3.7.1-1
- Version update

* Tue Oct 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.6.5-2
- fixed perms
* Tue Jul 29 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 3.6.5-1
- wrote new spec file
- updated to 3.6.5
- changed compiler to sun studio
- added patch to fix C99 compatability 
