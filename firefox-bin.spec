Summary: Mozilla Firefox
Name: mozilla-firefox-bin
Version: 1.5.0.1
Release: 3
Copyright: GPL
Group: Applications/Internet
Source: firefox-1.5.0.1.en-US.solaris2.8-sparc-gtk1.tar.bz2
URL: http://www.mozilla.org/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Conflicts: mozilla-firefox
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
if [ -e /usr/local/bin/firefox ]
	then
		mv /usr/local/bin/firefox /usr/local/bin/firefox.rpm
		cat<<EOF
Moving old /usr/local/bin/firefox to /usr/local/bin/firefox.rpm
EOF
fi
ln -s /usr/local/firefox/firefox /usr/local/bin/firefox
%ifos solaris2.9
cat<<EOF


The following patches MUST be installed in order for Firefox to work:
111711-11 32-Bit Shared library patch for C++
111712-11 64-Bit Shared library patch for C++
111722-04 SunOS 5.9: Math Library (libm) patch
112661-06 SunOS 5.9: IIIM and X Input & Output Method patch
112785-34 X11 6.6.1: Xsun patch
112963-10 SunOS 5.9: linker patch
113902-03 SunOS 5.9: Asian UTF-8 iconv modules enhancement
114276-02 SunOS 5.9: Extended Arabic support in UTF-8
114641-02 SunOS 5.9: Japanese iconv for UTF-8 patch
EOF
%endif
%ifos solaris2.8
cat<<EOF


The following patches MUST be installed in order for Firefox to work:
108434-17 32-Bit Shared library patch for C++
108435-17 64-Bit Shared library patch for C++
108652-79 X11 6.5.1: Xsun patch
108773-18 SunOS 5.8: IIIM and X Input & Output Method patch
109147-27 SunOS 5.8: linker patch
109159-03 SunOS 5.8: Chinese iconv module updates
109704-03 SunOS 5.8: Japanese iconv patch
111721-04 SunOS 5.8: Math Library (libm) patch
113261-02 SunOS 5.8: UTF-8 locale ICONV patch
114542-01 SunOS 5.8: Adds extended Arabic support
111721-04 SunOS 5.8: Math Library (libm) patch
EOF
%endif

%postun
rm /usr/local/bin/firefox

%files
%defattr(-,bin,bin)
/usr/local/firefox
/usr/local/bin

%changelog
* Sun Feb 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.0.1
- Updated to new version
* Thu Feb 02 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.0.1rc1-1
- Updated to new version
* Mon Dec 05 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5-3
- Fixed error in post section 
* Sat Dec 03 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5-1
- First release of Mozilla Firefox 1.5 binaries from ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/1.5/contrib/
