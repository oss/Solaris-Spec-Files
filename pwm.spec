Summary: P Window Manager
Name: pwm
Version: 1.0
Release: 2
License: Artistic
Group: Applications/X11
Source: pwm-%{version}.tar.gz
Patch: pwm.patch
BuildRoot: /var/tmp/%{name}-root

%description
PWM is a rather lightweight window manager that can have multiple
client windows attached to a single frame.  This feature helps keep
windows, especially the numerous xterms, organized.

(from the man page)

%prep
%setup -q
%patch 

%build
make

%install
rm -rf $RPM_BUILD_ROOT
for i in bin man/man1 etc/pwm ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done
install -c -m 755 pwm $RPM_BUILD_ROOT/usr/local/bin
strip $RPM_BUILD_ROOT/usr/local/bin/pwm
install -c -m 644 pwm.1x $RPM_BUILD_ROOT/usr/local/man/man1
for i in etc/pwm/*.conf ; do 
    install -c -m 644 $i $RPM_BUILD_ROOT/usr/local/$i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "To run pwm, you must copy the files in /usr/local/etc/pwm."

%files
%defattr(-,root,other)
%doc config.txt LICENSE
/usr/local/bin/pwm
/usr/local/man/man1/pwm.1x
/usr/local/etc/pwm
