Name: finger
Version: 1.37
Release: 3
Summary: GNU finger
Copyright: GPL
Group: Applications/Internet
Source: finger-1.37.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU finger is an exceedingly old finger server and client.  If you
want to use the GNU finger client, install this package.  (Install
finger-server if you want to use the server.)

%package server
Summary: GNU finger server
Group: Applications/Internet

%description server
Install this if you want to use GNU fingerd.  Examine the INSTALL file
located in the documentation tree for further instructions.

%prep
%setup -q

%build
perl -i -p -e 's/\$\(CC\)="\$\(CC\)"/CC=\$\(CC\)/' Makefile.in
./configure --prefix=/usr/local/gnu
make CC="gcc -R/usr/ucblib -D__EXTENSIONS__ -O"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu/bin
mkdir %{buildroot}/usr/local/gnu/etc
cp src/finger %{buildroot}/usr/local/gnu/bin
for i in fingerd in.fingerd in.cfingerd ; do
    cp src/$i %{buildroot}/usr/local/gnu/etc
done
cp doc/finger.info %{buildroot}/usr/local/gnu/info

%post server
[ -x /usr/local/bin/install-info ] && /usr/local/bin/install-info \
 --info-dir=/usr/local/gnu finger.info \
 --entry="* Finger: (finger).                         GNU finger" \
 finger.info

%preun server
[ -x /usr/local/bin/install-info ] && /usr/local/gnu/bin/install-info \
 --info-dir=/usr/local/gnu --delete finger.info

%files
%defattr(-,root,bin)
/usr/local/gnu/bin/finger

%files server
%defattr(-,root,bin)
%doc support/* doc/finger.dvi
/usr/local/gnu/etc/fingerd
/usr/local/gnu/etc/in.fingerd
/usr/local/gnu/etc/in.cfingerd
