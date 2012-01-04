%include perl-header.spec

Summary: 	Command-line tool for file retrieval via HTTP/FTP
Name: 		wget
Version: 	1.13.4
Release: 	1
Group: 		Applications/Internet
License: 	GPLv3
URL:            http://www.gnu.org/software/wget/
Source: 	http://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: 	openssl
BuildRequires:	openssl

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

./configure --with-ssl=openssl --disable-nls
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
%doc README NEWS AUTHORS COPYING MAILING-LIST ChangeLog
/usr/local/bin/wget
/usr/local/etc/wgetrc.rpm
/usr/local/man/man1/wget.1
/usr/local/share/info/wget.info

%changelog
* Wed Jan 04 2011 Joshua Matthews <jam761@nbcs.rutgers.edu -1.13.4
- bump version
* Mon Oct 05 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.12-1
- bump version
* Tue Jul 1 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.11.4-1
- Added, %doc entry, updated to version 1.11.4
* Tue Jun 24 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.11.3-2
- Disabled NLS 
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.11.3-1
- bumped version
