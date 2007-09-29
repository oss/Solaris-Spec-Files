%include perl-header.spec

Summary: 	Command-line tool for file retrieval via HTTP/FTP
Name: 		wget
Version: 	1.10.2
Release: 	7
Group: 		Applications/Internet
Copyright: 	GPL
Source: 	%{name}-%{version}.tar.gz
Patch:		wget.destdir.patch
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	openssl >= 0.9.8
BuildArch:	sparc64

%description
Wget is a network utility to retrieve files from the Web using http and 
ftp, the two most widely used Internet protocols. It works 
non-interactively, so it will work in the background, after having 
logged off. The program supports recursive retrieval of web-authoring 
pages as well as ftp sites-- you can use wget to make mirrors of 
archives and home pages or to travel the Web like a WWW robot.

Wget works particularly well with slow or unstable connections by 
continuing to retrive a document until the document is fully downloaded. 
Re-getting files from where it left off works on servers (both http and 
ftp) that support it. Both http and ftp retrievals can be time stamped, 
so wget can see if the remote file has changed since the last retrieval 
and automatically retrieve the new version if it has.

Wget supports proxy servers; this can lighten the network load, speed up 
retrieval, and provide access behind firewalls.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --with-libssl-prefix=/usr/local/ssl --prefix=/usr/local
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

%changelog
* Tue Dec 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.10.2-3
- Bumped for openssl 0.9.8
* Fri Jun 09 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.10.2-2
- Cleaned up spec file
