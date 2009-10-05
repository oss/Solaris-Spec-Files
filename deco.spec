Name:           deco
Version:        1.6.0.1
Release:        1%{?dist}
Summary:        Extractor for various archive file formats
Group:          Applications/Archiving
License:        GPLv3
URL:            http://hartlich.com/deco/
Source0:        http://hartlich.com/deco/download/%{name}-%{version}.tar.gz
Source1:        deco-stdbool.h
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       deco-archive >= 1.2

%description
deco is a Un*x program, written in SUSv3-compliant C99, 
that is able to extract various archive file formats
with features like consistent behavior, consistent 
interface and much more.

%prep
%setup -q
pwd
sed -i 's|<stdbool.h>|"stdbool.h"|' *
cp %{SOURCE1} ./stdbool.h


%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

make %{?_smp_mflags} PREFIX=%{_prefix} SHARE=%{_datadir}/%{name}-archive \
                     LDFLAGS="" CC="cc" CPPFLAGS=

%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE CREDITS NEWS README
%{_bindir}/%{name}

%changelog
* Fri Oct 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.0.1-1
- Solaris port

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6-1
- Version update. Change in work flow for failed extractions.

* Thu Nov 20 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.7-2
- License is GPLv3.
- The extraction scripts will be inside %%{_var}/lib/%%{name}.

* Wed Nov 19 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.7-1
- Version update

* Wed Oct 29 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.6-2
- Package deco-archive separately

* Tue Oct 28 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.6-1
- Rebuild with version 1.5.6

* Mon Apr 28 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.8.1-2
- Updates to file listings per review
- moved to macros instead of direct paths
- Source0 now in url form
- added dir for the deco data directory

* Fri Apr 25 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.8.1-1
- Upstream updates.
- Updates to file listings.

* Mon Apr 14 2008 Steve 'Ashcrow' Milner <stevem@gnulinux.net> - 0.6-1
- Initial package.

