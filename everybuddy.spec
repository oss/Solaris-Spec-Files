%include gnome-header.spec

Summary: AIM/jabber/yahoo etc. chat client
Name: everybuddy
Version: 0.2.1beta6
Release: 1
Group: Applications/Productivity
License: GPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: %{gnome_pkg}
BuildRequires: %{gnome_dev}

%description
Everybuddy is a chat program for X that incorporates the functions of AOL 
Instant Messenger, ICQ, Yahoo Chat, and MSN Messanger.  It's based on the 
following excellent libraries: 

        libmsn          Written by Shane P. Brady for Everybuddy Use.

        libicq          http://www.korsoft.com/gicq

        yahoolib        http://www.unixtools.com/gtkyahoo

        libtoc          Written by Torrey Searle for Everybuddy Use.

 (from README)

%prep
%setup -q

%build
CPPFLAGS="-I. -I./h" LDFLAGS="%{gnome_ldflags}" ./configure --disable-zephyr
%ifos solaris2.6
ed libxode/include/libxode.h <<EOF
   g/resolv\.h/s/resolv\.h/netdb.h/p
   w
   q
EOF
%endif
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}
if [ -r %{buildroot}/etc/X11/applnk/Internet/Everybuddy.desktop ]; then
    mkdir -p %{buildroot}/usr/local/share/gnome/apps/Internet
    mv %{buildroot}/etc/X11/applnk/Internet/Everybuddy.desktop \
        %{buildroot}/usr/local/share/gnome/apps/Internet
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,other)
/usr/local/share/pixmaps/ebicon.png
/usr/local/share/sounds/everybuddy
/usr/local/man/man1/everybuddy.1
/usr/local/bin/everybuddy
/usr/local/bin/update.pl
/usr/local/bin/contact-update.pl
/usr/local/share/gnome/apps/Internet/Everybuddy.desktop
