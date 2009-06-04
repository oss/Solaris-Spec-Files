Name: 		elinks
Summary: 	A text-mode Web browser.
Version: 	0.11.6
Release: 	2
Group:          Applications/Internet
License:	GPL
URL:            http://elinks.or.cz/

Source: 	http://elinks.or.cz/download/elinks-%{version}.tar.gz
Patch0:		elinks-0.11.4-conv.patch
Patch1:		elinks-0.11.6-wpwhois.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: 	pkgconfig, autoconf, automake
BuildRequires:	openssl, bzip2-devel, expat-devel
BuildRequires:	libidn-devel, zlib-devel, heimdal-devel
BuildRequires:	cyrus-sasl

Obsoletes:	links
Provides:	webclient, links

%description
Links is a text-based Web browser. Links does not display any images,
but it does support frames, tables and most other HTML tags. Links'
advantage over graphical browsers is its speed--Links starts and exits
quickly and swiftly displays Web pages.

%package -n wpwhois-elinks
Group:		Applications/Internet
Obsoletes:	wpwhois
Provides:	wpwhois
Summary:	White pages query tool

%description -n wpwhois-elinks
Wpwhois lets you look up Rutgers faculty and students from the command
line. 

%prep
%setup -q -n elinks-%{version}
cd src/util
%patch0 -p0
cd $RPM_BUILD_DIR
rm -rf elinks-%{version}-wpwhois
cp -r elinks-%{version} elinks-%{version}-wpwhois
cd elinks-%{version}-wpwhois
%patch1 -p1
cd ../elinks-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" 
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" 
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS 

#build elinks
./configure 				\
   	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--disable-nls 			\
   	--without-x 			\
   	--with-gssapi 			\
   	--disable-smb 			\
   	--with-openssl=%{_prefix}/ssl

gmake

#build wpwhois
cd ../elinks-%{version}-wpwhois
./configure                             \
        --prefix=%{_prefix}             \
        --mandir=%{_mandir}             \
        --disable-nls                   \
        --without-x                     \
        --with-gssapi                   \
        --disable-smb                   \
        --with-openssl=%{_prefix}/ssl

gmake

cd ../elinks-%{version}

%install
rm -rf %{buildroot}

#install elinks
gmake install DESTDIR=%{buildroot}
cd %{buildroot}%{_bindir}
ln -s elinks links

#install wpwhois
cd $RPM_BUILD_DIR/elinks-%{version}-wpwhois
%{__install} -m 0755 src/elinks %{buildroot}%{_bindir}/wpwhois
%{__install} -m 0644 wpwhois.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc README SITES TODO
%{_bindir}/links
%{_bindir}/elinks
%{_mandir}/man1/elinks.1
%{_mandir}/man5/*.5

%files -n wpwhois-elinks
%defattr(-, root, root)
%{_bindir}/wpwhois
%{_mandir}/man1/wpwhois.1

%changelog
* Thu Jun 04 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.6-2
- Added wpwhois (moved to elinks from lynx)
* Tue Apr 14 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.6-1
- Updated to version 0.11.6
- Removed two patches
- A symlink is now made (links --> elinks) instead of copying the executable
* Thu Aug 7 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.11.4-1
- patched to compile on sun cc
- first solaris release
