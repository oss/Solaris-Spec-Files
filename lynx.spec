Name: lynx
Version: 2.8.4
Copyright: GPL
Group: Applications/Internet
Summary: The popular web browser for terminals
Release: 2
Source: lynx%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
BuildRequires: openssl
Requires: openssl

%description 
Lynx is a text-based web browser.  You might want this package if you
want to browse the web or html documents but don't need to see images,
don't have enough free memory for Netscape, or if you don't have access
to X.

%prep
%setup -q -n lynx2-8-4

%build
./configure --prefix=/usr/local --with-ssl=/usr/local/ssl
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install-full prefix=%{buildroot}/usr/local
mv %{buildroot}/usr/local/lib/lynx.cfg \
   %{buildroot}/usr/local/lib/lynx.cfg.rpm

for i in COPYING COPYHEADER; do
    rm -f %{buildroot}/usr/local/lib/lynx_help/$i
    ln -s ../lynx_doc/$i %{buildroot}/usr/local/lib/lynx_help/$i
done

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Move /usr/local/lib/lynx.cfg.rpm to /usr/local/lib/lynx.cfg.
EOF

%files
%defattr(-,root,root)
/usr/local/bin/lynx
/usr/local/man/man1/lynx.1
/usr/local/lib/lynx.cfg.rpm
/usr/local/lib/lynx_help
/usr/local/lib/lynx_doc

