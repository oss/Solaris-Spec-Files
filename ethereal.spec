Name: ethereal
Version: 0.9.15
Release: 0
Summary: Ethereal packet sniffer
Source: http://www.ethereal.com/distribution/ethereal-%{version}.tar.bz2
Copyright: GPL
Group: Networking
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpcap
Packager: Rutgers University

%description
Pretty GTK packet sniffer.

%prep
%setup -q

%build
# Yay GNOME and multiple Solari.
# perl5 for pod2man
PATH=/opt/gnome-1.4/bin:/usr/sfw/bin:/opt/gnome-2.0/bin:/usr/local/gnu/bin:$PATH:/usr/local/perl5/bin:/usr/perl5/bin
export PATH
LDFLAGS='-L/opt/gnome-1.4/lib -R/opt/gnome-1.4/lib -L/opt/gnome-2.0/lib -R/opt/gnome-2.0/lib -L/usr/sfw/lib -R/usr/sfw/lib' ./configure --with-pcap=/usr/local --with-zlib --with-ssl=/usr/local/ssl

%install
PATH=/opt/gnome-1.4/bin:/usr/sfw/bin:/opt/gnome-2.0/bin:/usr/local/gnu/bin:$PATH:/usr/local/perl5/bin:/usr/perl5/bin
export PATH
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%doc README.hpux  README.linux  README.vmware
%doc README.aix  README.irix  README.tru64  README.win32
%doc README.bsd

/usr/local/bin/*
/usr/local/lib/ethereal
/usr/local/man/man1/*
/usr/local/share/ethereal
