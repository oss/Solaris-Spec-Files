%include perl-header.spec

Summary: Command-line tool for file retrieval via HTTP/FTP
Name: wget
Version: 1.10.2
Release: 1
Group: Applications/Internet
Copyright: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: openssl

%description

%prep
%setup -q

%build

CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWSpro/bin/CC' ./configure --with-libssl-prefix=/usr/local/ssl
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/man/man1
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/local/etc/wgetrc %{buildroot}/usr/local/etc/wgetrc.rpm
if [ ! -r %{buildroot}/usr/local/man/man1/wget.1 ]; then
    (cd doc; make wget.1 POD2MAN=%{perl_prefix}/bin/pod2man)
    install -m 0644 doc/wget.1 %{buildroot}/usr/local/man/man1/wget.1
fi

%clean
rm -rf %{buildroot}

%post
echo "Edit and copy /usr/local/etc/wgetrc.rpm."
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info /usr/local/info/wget.info \
        --info-dir=/usr/local/info
fi

%preun
if [ -x /usr/local/bin/install-info ]; then
    /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	/usr/local/info/wget.info
fi


%files
%defattr(-,root,root)
/usr/local/bin/wget
/usr/local/info/wget.info*
/usr/local/etc/wgetrc.rpm
/usr/local/share/locale/*/LC_MESSAGES/wget.mo
/usr/local/man/man1/wget.1
