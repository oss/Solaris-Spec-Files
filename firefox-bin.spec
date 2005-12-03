Summary: Mozilla Firefox
Name: mozilla-firefox-bin
Version: 1.5
Release: 2
Copyright: GPL
Group: Applications/Internet
Source: firefox1.5-en-US.solaris2.8-sparc-gtk1.tar.bz2
URL: http://www.mozilla.org/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Obsoletes: mozilla-firebird FireFox phoenix mozilla-firefox < 1.5
Provides: webclient libCstd.so.1

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
%setup -q -n firefox

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cd ..
mkdir -p firefox/extensions/talkback@mozilla.org
touch firefox/extensions/talkback@mozilla.org/chrome.manifest
cp -R firefox $RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -s /usr/local/firefox/firefox /usr/local/bin/firefox
%ifos solaris2.9
echo "The following patches MUST be installed in order for Firefox to work"
echo "111711-11 32-Bit Shared library patch for C++"
echo "111712-11 64-Bit Shared library patch for C++"
echo "111722-04 SunOS 5.9: Math Library (libm) patch"
echo "112661-06 SunOS 5.9: IIIM and X Input & Output Method patch"
echo "112785-34 Xecho "11 6.6.1: Xsun patch"
echo "112963-10 SunOS 5.9: linker patch"
echo "113902-03 SunOS 5.9: Asian UTF-8 iconv modules enhancement"
echo "114276-02 SunOS 5.9: Extended Arabic support in UTF-8"
echo "114641-02 SunOS 5.9: Japanese iconv for UTF-8 patch"
echo "111722-04 SunOS 5.9: Math Library (libm) patch
%endif
%ifos solaris2.8
echo "The following patches MUST be installed in order for Firefox to work"
echo "108434-17 32-Bit Shared library patch for C++"
echo "108435-17 64-Bit Shared library patch for C++"
echo "108652-79 X11 6.5.1: Xsun patch"
echo "108773-18 SunOS 5.8: IIIM and X Input & Output Method patch"
echo "109147-27 SunOS 5.8: linker patch"
echo "109159-03 SunOS 5.8: Chinese iconv module updates"
echo "109704-03 SunOS 5.8: Japanese iconv patch"
echo "111721-04 SunOS 5.8: Math Library (libm) patch"
echo "113261-02 SunOS 5.8: UTF-8 locale ICONV patch"
echo "114542-01 SunOS 5.8: Adds extended Arabic support"
echo "111721-04 SunOS 5.8: Math Library (libm) patch"
%endif

%postun
rm /usr/local/bin/firefox

%files
%defattr(-,bin,bin)
/usr/local/firefox
/usr/local/bin

%changelog
* Mon Oct 03 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5-1
- First release of Mozilla Firefox 1.5 binaries from ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/1.5/contrib/
