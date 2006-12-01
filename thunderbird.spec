Summary: 	Mozilla Thunderbird mail/news client.
Name: 		mozilla-thunderbird
Version: 	1.5.0.8
Release: 	1
License: 	GPL
Group: 		Applications/Internet
URL: 		http://www.mozilla.org/projects/thunderbird/
Packager:	Eric Rivas <kc2hmv@nbcs.rutgers.edu>
Vendor: 	NBCS-OSS
Distribution: 	RU-Solaris
Source:		thunderbird-%{version}-source.tar.bz2
Patch0: firefox-1.5-HellNoGNOME.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: autoconf213 = 2.13
BuildRequires: cairo-devel >= 1.2.4
BuildRequires: expat-devel >= 2.0.0
BuildRequires: fontconfig-devel >= 2.3.95
BuildRequires: gtk2-devel >= 2.10
BuildRequires: libIDL2 >= 0.8
BuildRequires: make >= 3.19.1
BuildRequires: perl >= 5.6
BuildRequires: pkgconfig >= 0.21
BuildRequires: xft2-devel >= 2.1.7
BuildRequires: libpng3-devel >= 1.2.8
BuildRequires: openldap-lib
BuildConflicts: nss
BuildConflicts: nspr
Requires: cairo >= 1.2.4
Requires: expat >= 2.0.0
Requires: gtk2 >= 2.10
Requires: fontconfig >= 2.3.95
Requires: xft2 >= 2.1.7
Requires: libpng3 >= 1.2.8
Requires: openldap-lib

%description
Mozilla Thunderbird is a redesign of the Mozilla mail component.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n mozilla
%patch0 -p1

%build

cat << EOF > .mozconfig
mk_add_options MOZ_CO_PROJECT=mail
mk_add_options MOZ_MAKE_FLAGS=-j8

ac_add_options --enable-application=mail
ac_add_options --enable-xft
ac_add_options --enable-svg
ac_add_options --enable-canvas
ac_add_options --enable-static
ac_add_options --enable-optimize=-xO3
ac_add_options --enable-official-branding
ac_add_options --enable-default-toolkit=gtk2
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --disable-shared
ac_add_options --disable-auto-deps
ac_add_options --disable-freetype2
ac_add_options --disable-ldap

EOF

PATH="/usr/local/gnu/bin:/usr/local/bin:$PATH" \
CC="cc" \
CXX="CC" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lnsl" \
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export PATH CC CXX CPPFLAGS LDFLAGS LIBIDL_CONFIG

# I think configure is dumb, so we have to tell the linker about these
LDFLAGS="${LDFLAGS} -lfontconfig -lXft"
export LDFLAGS

./configure

gmake -f client.mk build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/local/bin/*
/usr/local/lib/thunderbird-%{version}

%files devel
%defattr(0755,root,root)
/usr/local/include/thunderbird-%{version}
/usr/local/lib/pkgconfig/*
/usr/local/share/*

%changelog
* Tue Apr 18 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5-1
- New version

* Fri Jun 4 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.6-1
- New version

* Wed Feb 25 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.5-1
- Initial package
