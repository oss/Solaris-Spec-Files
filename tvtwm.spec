Summary: Tom's virtual Tab Window Manager
Name: tvtwm
Version: pl11
Release: 4
Copyright: BSD-type
Group: User Interface/X
Source0: tvtwm.pl11.tar.gz
Source1: tvtwm-bitmaps.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: xpm
BuildRequires: xpm

%description
tvtwm is a superset of the X11R5 release of twm (Tom's Window Manager),
written by Tom LaStrange.  Much of the early functionality, which is
described in more detail in README.old, was added by Tom LaStrange himself.
Since then, tvtwm has fallen under my control, and I've added some things
myself.

  The major benefit of tvtwm over twm is the "Virtual Desktop".  This
allows you do define a substitute root window that is larger than your
display area.  This new virtual root window is the parent for all of your
X clients.  tvtwm provides a "Panner" which will let you see a scaled down
representation of the whole virtual desktop.  Using this panner, and keys
bound to functions added to tvtwm, you can move around this desktop to
have your physical display showing only part of the whole desktop.  Thus,
you can have sections of your desktop assigned to particular tasks, or
just use it to keep from having 20 million layers of windows.  :-)

   [from tvtwm README]

%prep
%setup -q -n tvtwm

%build
xmkmf -a
make CC=gcc PICFLAGS="-fpic" \
   CCOPTIONS="-O -I/usr/local/include/X11 -I/usr/local/include \
              -L/usr/local/lib -R/usr/local/lib" \
   EXTRALDOPTIONS="-L/usr/local/lib -R/usr/local/lib"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/openwin/lib/X11/twm
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/man/man1
install -m 0755 tvtwm %{buildroot}/usr/local/bin/tvtwm
install -m 0444 system.twmrc \
    %{buildroot}/usr/openwin/lib/X11/twm/system.twmrc.rpm
install -m 0444 tvtwm.man %{buildroot}/usr/local/man/man1/tvtwm.1
mkdir -p %{buildroot}/usr/openwin/include/X11
cd %{buildroot}/usr/openwin/include/X11
gzip -dc %{_sourcedir}/tvtwm-bitmaps.tar.gz | tar xf -
chmod 0644 bitmaps/*
chmod 0755 bitmaps

%post
cat <<EOF
You have to edit and copy /usr/openwin/lib/X11/twm/system.twmrc.rpm.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/openwin/include/X11/bitmaps/*
/usr/openwin/lib/X11/twm/system.twmrc.rpm
/usr/local/bin/tvtwm
/usr/local/man/man1/tvtwm.1
