Summary: 	Mozilla Thunderbird mail/news client.
Name: 		mozilla-thunderbird
Version: 	0.6
Release: 	1
License: 	GPL
Group: 		Applications/Internet
URL: 		http://www.mozilla.org/projects/thunderbird/
Packager:	Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
Vendor: 	NBCS-OSS
Distribution: 	RU-Solaris
Source:		thunderbird-0.6-source.tar.bz2
#Source:	http://ftp24moz.newaol.com/pub/mozilla.org/thunderbird/releases/0.6/thunderbird-0.6-source.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

%description
Mozilla Thunderbird is a redesign of the Mozilla mail component.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use {%name}.

%prep
%setup -n mozilla

CPPFLAGS="-I/usr/sfw/include/glib-1.2 -I/usr/sfw/lib/glib/include -I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib/ -R/usr/local/lib -L/usr/local/lib/mozilla-1.6 -R/usr/local/lib/mozilla-1.6 -lglib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib:/usr/local/lib/mozilla-1.6"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib:/usr/local/lib/mozilla-1.6"
CC="gcc -O3 -pipe -s -fforce-addr"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
MOZ_THUNDERBIRD="1"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH MOZ_THUNDERBIRD

./configure \
	--with-system-jpeg \
	--with-system-zlib \
	--with-system-png \
	--with-system-mng \
	--with-pthreads \
	--disable-tests \
	--disable-debug \
	--disable-mathml \
	--disable-installer \
	--disable-activex \
	--disable-activex-scripting \
	--disable-oji \
	--disable-necko-disk-cache \
	--disable-profilesharing \
	--enable-optimize="%{optflags}" \
	--enable-crypto \
	--enable-strip \
	--enable-strip-libs \
	--enable-reorder \
	--enable-xinerama \
	--enable-extensions="wallet,spellcheck,xmlextras" \
	--enable-necko-protocols="http,file,jar,viewsource,res,data" \
	--enable-image-decoders="png,gif,jpeg,bmp" \
        --enable-default-toolkit=gtk \
	--with-libidl-prefix=/usr/local

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/local/lib/thunderbird-0.6/*
/usr/local/bin/*

%files devel
%defattr(0755,root,root)
/usr/local/include/thunderbird-0.6/*
/usr/local/lib/pkgconfig/*
/usr/local/share/*

%changelog
* Fri Jun 4 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.6-1
- New version

* Wed Feb 25 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.5-1
- Initial package
