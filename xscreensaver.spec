%include gnome-header.spec

Name: xscreensaver
Version: 3.34
Copyright: Freely distributable
Group: Amusements/Graphics
Summary: Screensaver for X11
Release: 1
Source: xscreensaver-%{version}.tar.gz
Requires: emacs = 20.7
Requires: xpm
BuildRoot: /var/tmp/%{name}-root
BuildRequires: xpm
BuildRequires: %{gnome_dev}
BuildRequires: perl

%description
Xscreensaver is a collection of screensavers for X11.

%prep
%setup -q

%build
PATH="/usr/local/bin:$PATH" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib %{gnome_ldflags}" \
  CPPFLAGS="-I/usr/local/include %{gnome_cppflags}" \
  ./configure --prefix=/usr/local --with-xpm \
  --with-zippy=/usr/local/emacs20/libexec/emacs/20.7/%{sparc_arch}/yow \
  --with-pam --without-gnome --without-gl --without-gle
perl -i -p -e 's#^(SUBDIRS.*)hacks/glx#$1#' Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/
for i in utils driver hacks ; do 
    (cd $i && make install prefix=$RPM_BUILD_ROOT/usr/local)
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To enable locking, you need to add a line to /etc/pam.conf that looks
something like

xscreensaver    auth sufficient /usr/lib/security/pam_ru.so.1

You may want to have another terminal nearby, so you can telnet in if
xscreensaver does not lock properly.
EOF

%files
%defattr(-,bin,bin)
%doc README
/usr/local/bin/*
/usr/local/man/man1/*
