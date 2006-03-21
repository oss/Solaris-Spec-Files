Name: aspell
Summary: aspell spelling checker
Version: 0.60.4
Release: 2
Copyright: GPL
Group: Applications/Spelling
Source: http://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
URL: http://aspell.net/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

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

%build
CC="gcc"
CXX="g++"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
export CC CXX LDFLAGS CPPFLAGS
./configure --disable-nls \
            --disable-wide-curses \
            --enable-curses="-L/usr/lib -lcurses" \
            --enable-curses-include=/usr/include
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}
# remove info dir
rm %{buildroot}/usr/local/info/dir
# remove *.la files
rm %{buildroot}/usr/local/lib/libaspell.la
rm %{buildroot}/usr/local/lib/libpspell.la

%post
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/aspell.info
        /usr/local/bin/install-info --info-dir=/usr/local/info /usr/local/info/aspell-dev.info
fi

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
/usr/local/info/*
/usr/local/lib/aspell-0.60/*
/usr/local/lib/*.so*
/usr/local/man/man1/*.1

%changelog
* Mon Mar 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 0.60.4-1
- Upgrade to the latest version and built against new gcc-3.4.5

