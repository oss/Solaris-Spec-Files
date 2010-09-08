%global deco_archive_ver 1.5.1

Name:           deco
Version:        1.6.2
Release:        2%{?dist}
Summary:        Extractor for various archive file formats
Group:          Applications/Archiving
License:        GPLv3
URL:            http://hartlich.com/deco/
Source0:        http://hartlich.com/deco/download/%{name}-%{version}.tar.gz
Source1:        http://hartlich.com/deco/archive/download/deco-archive-%{deco_archive_ver}.tar.gz
Source2:        deco-stdbool.h
Patch0:         unset_env2.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Obsoletes:       deco-archive < 1.5-4
Provides:        deco-archive = %{deco_archive_ver}

%description
deco is a Un*x program, written in SUSv3-compliant C99, 
that is able to extract various archive file formats
with features like consistent behavior, consistent 
interface and much more.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE2} ./stdbool.h
tar zxf %{SOURCE1}


%build
export PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
gmake %{?_smp_mflags} PREFIX=%{_prefix} SHARE=%{_datadir}/%{name} \
      		      CC="cc" CXX="CC" \
		      CFLAGS="-I/usr/local/include -I. -g -xO2" \
		      CPPFLAGS="-I/usr/local/include -I. -g -xO2" \
		      LDFLAGS="-L/usr/local/lib -R/usr/local/lib"

%install
rm -rf %{buildroot}
gmake install PREFIX=%{_prefix} DESTDIR=%{buildroot}

pushd deco-archive-%{deco_archive_ver}
   gmake install DESTDIR=%{buildroot} SHARE=%{_datadir}/%{name}
   for file in LICENSE CREDITS NEWS README; do
       mv $file ../$file.deco-archive
   done
popd

%clean
rm -rf %{buildroot}

%post
echo deco can decompress a variety of archive formats. For more functionality,
echo install bzip2, cpio, tar, xz, xz-lzma-compat, ...


%files
%defattr(-,root,root,-)
%doc LICENSE* CREDITS* NEWS* README*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Sep 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.2-2
- Update unset_env patch

* Wed Aug 25 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.2-1
- Update to 1.6.2

* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.0.1-4
- I will not publish unsigned packages again

* Mon Nov 30 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.0.1-3
- Rebuild. Something wrong with the gpg key

* Fri Oct 09 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.0.1-2
- Unify deco and deco-archive

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

