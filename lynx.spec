%define sversion 2-8-6

Name: lynx
Version: 2.8.6rel.5
Copyright: GPL
Group: Applications/Internet
Summary: The popular web browser for terminals
Release: 1
Patch: wpwhois.patch
Source: %{name}%{version}.tar.gz
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}%{version}
BuildRequires: openssl slang-devel
Requires: openssl slang
BuildConflicts: gd-devel

%description
Lynx is a text-based web browser.  You might want this package if you
want to browse the web or html documents but don't need to see images,
don't have enough free memory for Firefox, or if you don't have access
to X.

%package -n wpwhois 
Group: Applications/Internet
Summary: White pages query tool
Requires: %{name} = %{version}
%description -n wpwhois
Wpwhois lets you look up Rutgers faculty and students from the command
line.

%prep
%setup -q -c -n lynx%{version}
cp -r lynx%{sversion} lynx%{sversion}-wpwhois 
cd lynx%{sversion}-wpwhois 
%patch -p1
cd ..

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

#make lynx
cd lynx%{sversion}
./configure --prefix=/usr/local --with-ssl=/usr/local/ssl --with-screen=slang --enable-exec-links --enable-exec-scripts --enable-change-exec --enable-externs
gmake

#make wpwhois 
cd ../lynx%{sversion}-wpwhois 
./configure --prefix=/usr/local --with-ssl=/usr/local/ssl --with-screen=slang --enable-exec-links --enable-exec-scripts --enable-change-exec --enable-externs
gmake

cd ..

%install 
rm -rf %{buildroot}
mkdir -p %{buildroot}

#install lynx
cd lynx%{sversion}
gmake install-full DESTDIR=%{buildroot}
gmake install-help DESTDIR=%{buildroot}
gmake install-doc DESTDIR=%{buildroot}

for i in COPYING COPYHEADER; do
    rm -f %{buildroot}/usr/local/share/lynx_help/$i
    ln -s ../lynx_doc/$i %{buildroot}/usr/local/share/lynx_help/$i
done
gmake clean

#install wpwhois 
cd ../lynx%{sversion}-wpwhois 
install -m 0755 lynx %{buildroot}/usr/local/bin/wpwhois
install -m 0644 wpwhois.1 %{buildroot}/usr/local/man/man1/wpwhois.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc /usr/local/share/lynx_doc
%doc /usr/local/share/lynx_help
/usr/local/bin/lynx
/usr/local/man/man1/lynx.1
%config(noreplace) /usr/local/etc/lynx.cfg

%files -n wpwhois
%defattr(-,root,root)
/usr/local/bin/wpwhois
/usr/local/man/man1/wpwhois.1

%changelog
* Thu Jul 3 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.8.6rel.5-1
- Updated to version 2.8.6rel.5
- Note that 2.8.6rel.5 is an official release, the source from our previous 
  release (2.8.6-1) is the same as from release 2.8.6rel.4-1; a lynx development 
  release would have 'dev' instead of 'rel' in the version
* Fri Apr 06 2007 John M. Santel <jmsl@nbcs.rutgers.edu> - 2.8.6-1
 - Bumped to official release and integrated wpwhois patch
* Tue Dec 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.8.6rel.4-1
 - Bumped for openssl 0.9.8
* Fri Jul 19 2005 John M. Santel <jmsl@nbcs.rutgers.edu> - 2.8.5-2
- Removed %pre and fixed %post to comply with configuration policy.
  %config(noreplace) is used instead of doing shell hacks to backup  
  lynx.cfg. This is much less evil. 
* Fri Jul 12 2005 John M. Santel <jmsl@nbcs.rutgers.edu> - 2.8.5-1 
- updated to 2.8.5. Added a pre section to detect the existence of an
  existing configuration file and back it up before replacement. 
  The original spec file installed lynx.cfg.rpm to prevent overwriting an 
  exisiting configuration. However, if this was a fresh install, it would 
  leave the machine with no usable default configuration, since lynx.cfg.rpm
  could not be found at runtime.  
