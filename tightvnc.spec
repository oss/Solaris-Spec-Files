Summary:	A remote display system.
Name:		tightvnc
Version:	1.3.8
Release:	1
URL:		http://www.tightvnc.com/
Source0:	tightvnc-%{version}_unixsrc.tar.gz
License:	GPL
Group:		User Interface/Desktops
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Obsoletes:	vnc
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildPrereq:	tcp_wrappers
BuildRequires:	zlib-devel libjpeg-devel

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures. TightVNC is an enhanced
VNC distribution. This package contains a client which will allow you
to connect to other desktops running a VNC or a TightVNC server.

%package server
Summary: TightVNC server
Obsoletes: vnc-server
Requires: bash >= 2.0
Group: User Interface/X
Prereq: /sbin/chkconfig /sbin/service /etc/init.d

%description server
The VNC system allows you to access the same desktop from a wide
variety of platforms. TightVNC is an enhanced VNC distribution. This
package is a TightVNC server, allowing others to access the desktop on
your machine.

%prep
%setup -q -n vnc_unixsrc

perl -pi -e "s|/usr/local/vnc/classes|%{_datadir}/vnc/classes|" vncserver

%build
# Use xinit's Xclients script to start the session (bug #52711)
patch < vnc-xclients.patch

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/lib -R/usr/lib -lwrap \
-lnss_nis"
export PATH CC CXX CPPFLAGS LD LDFLAGS

xmkmf -a
make World

cd Xvnc
./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
./vncinstall %{buildroot}%{_bindir} %{buildroot}%{_mandir}

mkdir -p %{buildroot}%{_datadir}/vnc
cp -pR classes %{buildroot}%{_datadir}/vnc

strip %{buildroot}%{_bindir}/* || :

mkdir -p %{buildroot}/etc/rc.d/init.d
install -m755 vncserver.init %{buildroot}/etc/rc.d/init.d/vncserver

mkdir -p %{buildroot}/etc/sysconfig
cat > %{buildroot}/etc/sysconfig/vncservers << EOF
# The VNCSERVERS variable is a list of display:user pairs.
#
# Uncomment the line below to start a VNC server on display :1
# as my 'myusername' (adjust this to your own).  You will also
# need to set a VNC password; run 'man vncpasswd' to see how
# to do that.  
#
# DO NOT RUN THIS SERVICE if your local area network is
# untrusted!  For a secure way of using VNC, see
# <URL:http://www.uk.research.att.com/vnc/sshvnc.html>.

# VNCSERVERS="1:myusername"
EOF
chmod 644 %{buildroot}/etc/sysconfig/vncservers

mkdir -p %{buildroot}/etc/X11/applnk/Applications
cat > %{buildroot}/etc/X11/applnk/Applications/vncviewer.desktop << EOF
[Desktop Entry]
Name=VNC Viewer
Comment=VNC client application
Exec=/usr/bin/vncviewer
Terminal=0
Type=Application
EOF

%clean
rm -rf %{buildroot}

%post server
if [ "$1" = 1 ]; then
  /sbin/chkconfig --add vncserver
fi

%preun server
if [ "$1" = 0 ]; then
  /sbin/service vncserver stop >/dev/null 2>&1
  /sbin/chkconfig --del vncserver
fi

%postun server
if [ "$1" -ge "1" ]; then
  /sbin/service vncserver condrestart >/dev/null 2>&1
fi

%files
%defattr(-,root,root)
%doc LICENCE.TXT README WhatsNew ChangeLog
%{_bindir}/vncviewer
%config(noreplace) /etc/X11/applnk/Applications/vncviewer.desktop
%{_mandir}/man1/vncviewer.1*

%files server
%defattr(-,root,root)
%doc LICENCE.TXT README WhatsNew ChangeLog
%attr(0755,root,root) %config /etc/rc.d/init.d/vncserver
%config(noreplace) /etc/sysconfig/vncservers
%{_bindir}/Xvnc
%{_bindir}/vncserver
%{_bindir}/vncpasswd
%{_bindir}/vncconnect
%{_datadir}/vnc
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncserver.1*
%{_mandir}/man1/vncconnect.1*
%{_mandir}/man1/vncpasswd.1*

%changelog
* Wed Sep 20 2006 David Lee Halik <dhalik@nbcs.rutgers.edu>
- Initial Solaris Sparc64 Build Version 1.3.8

