Name:           deco-archive
Version:        1.5
Release:        3%{?dist}
Summary:        Extraction scripts for various archive formats for use of deco
Group:          Applications/Archiving
License:        GPLv3
URL:            http://hartlich.com/deco/
Source0:        http://hartlich.com/deco/archive/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       coreutils,cpio,rpm,tar
Requires:       deco >= 1.5.6

%description
deco-archive provides support for popular archive 
formats to the deco file extraction framework.

%prep
%setup -q

%build
echo "Nothing to build."

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot} SHARE=%{_datadir}/%{name}


%files
%defattr(-,root,root,-)
%doc LICENSE CREDITS NEWS README
%{_datadir}/%{name}

%changelog
* Mon Oct 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5-3
- Solaris port

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 09 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5-1
- Version update. New extensions: deb, udeb, tar.xz, txz, xz
- Handle .lzma via xz-lzma-compat from now on

* Sat Apr 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.4-3
- Handle .zoo format with unzoo (if installed)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.4-1
- Version update. New extensions: gem and tbz2
- Handle .shn format (shorten) with ffmpeg (if installed)
- Handle .alz format with unalz (if installed)

* Fri Dec 12 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-1
- Version update
- Use ffmpeg instead of wine+Monkey's Audio for converting ape to wav

* Mon Dec 01 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-6
- Code cleanup

* Sun Nov 30 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-5
- Workaround for the "broken ghosts".

* Sun Nov 30 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-4
- Fixed a typo in the %%do_trigger* of tar\.lzma
- Added rpm to the default list
- Attempted to mark the non-default archivers as ghosts

* Thu Nov 20 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-3
- License is GPLv3.
- Install the scripts in %%{_datadir}/%%{name} and the symlinks in %%{var}/lib/deco.

* Wed Nov 19 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-2
- Added conditionals to the trigger functions to suppress warnings on updates.

* Wed Oct 29 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-1
- Initial build.
