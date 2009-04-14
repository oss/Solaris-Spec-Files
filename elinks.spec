Name: 		elinks
Summary: 	A text-mode Web browser.
Version: 	0.11.6
Release: 	1
Group:          Applications/Internet
License:	GPL
URL:            http://elinks.or.cz/

Source: 	http://elinks.or.cz/download/elinks-%{version}.tar.gz
Patch:		elinks-0.11.4-conv.patch
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

%prep
%setup -q -n %{name}-%{version}
cd src/util
%patch -p0
cd ../../

%build
PATH="/opt/SUNWspro/bin:${PATH}" 
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" 
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS 

./configure 				\
   	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--disable-nls 			\
   	--without-x 			\
   	--with-gssapi 			\
   	--disable-smb 			\
   	--with-openssl=%{_prefix}/ssl

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
cd %{buildroot}%{_bindir}
ln -s elinks links

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README SITES TODO
%{_bindir}/links
%{_bindir}/elinks
%{_mandir}/man1/elinks.1
%{_mandir}/man5/*.5

%changelog
* Tue Apr 14 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.6-1
- Updated to version 0.11.6
- Removed two patches
- A symlink is now made (links --> elinks) instead of copying the executable
* Thu Aug 7 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.11.4-1
- patched to compile on sun cc
- first solaris release
