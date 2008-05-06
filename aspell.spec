Name:		aspell
Summary:	aspell spelling checker
Version:	0.60.6
Release:	1
Copyright:	GPL
Group:		Applications/Spelling
Source:		http://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
#Patch0:		aspell-01-forte.diff
URL:		http://aspell.net/
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root

%description
GNU Aspell is a spell checker designed to eventually replace Ispell. It can
either be used as a library or as an independent spell checker. Its main
feature is that it does a superior job of suggesting possible replacements
for a misspelled word than just about any other spell checker out there for
the English language. Unlike Ispell, Aspell can also easily check documents
in UTF-8 without having to use a special dictionary. Aspell will also do its
best to respect the current locale setting. Other advantages over Ispell
include support for using multiple dictionaries at once and intelligently
handling personal dictionaries when more than one Aspell process is open at
once.

%prep
%setup -q
#%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lm" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --disable-nls \
            --disable-wide-curses \
            --enable-curses="-L/usr/lib -lcurses" \
            --enable-curses-include=/usr/include
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}
# remove info dir
#rm %{buildroot}/usr/local/info/dir
# remove *.la files
rm %{buildroot}/usr/local/lib/libaspell.la
rm %{buildroot}/usr/local/lib/libpspell.la
rm %{buildroot}/usr/local/share/info/dir

chmod -R 755 $RPM_BUILD_ROOT/usr/local/lib/aspell*

%post
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/aspell.info
        /usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/aspell-dev.info
fi

cat<<EOF

You NEED to install aspell-en for aspell to actually do any spell
checking.

EOF

%preun
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
                /usr/local/info/aspell.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
                /usr/local/info/aspell-dev.info
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,other)
%doc COPYING README TODO
/usr/local/bin/*
/usr/local/include/aspell.h
/usr/local/include/pspell/pspell.h
/usr/local/share/info/aspell-dev.info
/usr/local/share/info/aspell.info
#/usr/local/share/info/dir
/usr/local/share/man/man1/aspell-import.1
/usr/local/share/man/man1/aspell.1
/usr/local/share/man/man1/prezip-bin.1
/usr/local/share/man/man1/pspell-config.1
/usr/local/share/man/man1/run-with-aspell.1
/usr/local/share/man/man1/word-list-compress.1
/usr/local/lib/aspell-0.60/*
/usr/local/lib/*.so*

%changelog
* Thu Apr 24 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.60.6-1
- bumped to 0.60.6, switched to gmake, removed forte patch,
- rm usr/local/share/info/dir - file conflict
* Fri Aug 03 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.60.5-2
- Fixed file info
* Thu Aug 02 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.60.5-1
- Bump
* Thu Aug 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.60.4-5
- Switched over to Sun CC
* Mon Mar 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.60.4-1
- Upgrade to the latest version and built against new gcc-3.4.5

