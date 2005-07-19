Name: lynx
Version: 2.8.5
Copyright: GPL
Group: Applications/Internet
Summary: The popular web browser for terminals
Release: 1
Source: %{name}%{version}.tar.bz2
Packager: John Santel <jmsl@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}%{version}
BuildRequires: openssl slang-devel
Requires: openssl slang

%description 
Lynx is a text-based web browser.  You might want this package if you
want to browse the web or html documents but don't need to see images,
don't have enough free memory for Netscape, or if you don't have access
to X.

%prep
%setup -q -n lynx2-8-5

%build
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local --with-ssl=/usr/local/ssl --with-screen=slang
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install-full  prefix=%{buildroot}/usr/local
gmake install-help  prefix=%{buildroot}/usr/local
gmake install-doc prefix=%{buildroot}/usr/local

for i in COPYING COPYHEADER; do
    rm -f %{buildroot}/usr/local/lib/lynx_help/$i
    ln -s ../lynx_doc/$i %{buildroot}/usr/local/lib/lynx_help/$i
done

%pre
if [ -f /usr/local/lib/lynx.cfg ] ; then
  mv /usr/local/lib/lynx.cfg /usr/local/lib/lynx.cfg.rpm
fi 

%post 
if [ -f /usr/local/lib/lynx.cfg.rpm ] ; then
cat << EOF
  /usr/local/lib/lynx.cfg has been backed up to /usr/local/lib/lynx.cfg.rpm 
  and replaced with a new version. If you wish to restore your original 
  configuration, you should echo copy /usr/lib/local/lynx.cfg.rpm 
  to /usr/lib/local/lynx.cfg
EOF
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/lynx
/usr/local/man/man1/lynx.1
/usr/local/lib/lynx.cfg
/usr/local/lib/lynx_help
/usr/local/lib/lynx_doc

%changelog
* Fri Jul 12 2005 John M. Santel <jmsl@nbcs.rutgers.edu> - 2.8.5 
- updated to 2.8.5. Added a pre section to detect the existence of an
  existing configuration file and back it up before replacement. 
  The original spec file installed lynx.cfg.rpm to prevent overwriting an 
  exisiting configuration. However, if this was a fresh install, it would 
  leave the machine with no usable default configuration, since lynx.cfg.rpm
  could not be found at runtime.  


