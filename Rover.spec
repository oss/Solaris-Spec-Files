Summary: Rover network management tool
Name: Rover
Version: 4.0
Release: 2
Group: Applications/Internet
Copyright: BSD-type
Source: Rover4.0.tar.Z
Patch: Rover.patch
BuildRoot: /var/tmp/%{name}-root

%description
The Internet Rover Package is a simple network management package that
is based on the empirical notion that network operators only want to
know when something breaks. Flashy network topology maps may look
great for NOC tours, but fundamentally, the NOC Operators job is to
fix things when they break. So ideally, the NOC operators see a blank
screen when all is running fine, and a to-do list of what needs to be
fixed when the network is broken.

%prep
%setup -q -n Rover4
%patch -p1

%build
rm config.cache
./configure
make clean
echo "4.0" > VERSION
make src

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/rover/bin
mkdir -p $RPM_BUILD_ROOT/var/etc
make install BINDIR=$RPM_BUILD_ROOT/usr/local/rover/bin \
    ETCDIR=$RPM_BUILD_ROOT/var/etc
for i in rover.crontab mib.txt mib_desc distroverfile ; do
    mv $RPM_BUILD_ROOT/var/etc/$i $RPM_BUILD_ROOT/var/etc/$i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To finish installing Rover, first copy and edit

   /var/etc/rover.crontab.rpm
   /var/etc/mib.txt.rpm
   /var/etc/mib_desc.rpm
   /var/etc/distroverfile.rpm

Then run make root-install in /usr/local/rover/bin as root.
EOF

%files
%defattr(-,bin,bin)
/var/etc/Help/bogus
/var/etc/Help/host
/var/etc/rover.crontab.rpm
/var/etc/mib.txt.rpm
/var/etc/mib_desc.rpm
/var/etc/distroverfile.rpm
/var/etc/VERSION
/usr/local/rover/bin/*
