Name: ncftp
Version: 3.0.3
Release: 2
Copyright: Artistic
Group: Applications/Internet
Summary: FTP tools
Source: ncftp-%{version}-src.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Ncftp is a powerful ftp client with readline support, batch
downloading, bookmarks, and other features.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/man/man1/*
