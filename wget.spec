%include perl-header.spec

Summary: 	Command-line tool for file retrieval via HTTP/FTP
Name: 		wget
Version: 	1.11.3
Release: 	2
Group: 		Applications/Internet
Copyright: 	GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	openssl

%description

%prep
%setup -q

%build

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure --with-ssl=/usr/local/ssl --disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/man/man1
gmake install DESTDIR=%{buildroot}
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
/usr/local/etc/wgetrc.rpm
/usr/local/man/man1/wget.1
/usr/local/share/info/wget.info

%changelog
* Tue Jun 24 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.11.3-2
- Disabled NLS 
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.11.3-1
- bumped version
