%include machine-header.spec

Summary: Squeak Smalltalk development environment
Name: Squeak
Version: 2.7
Release: 2
Group: Development/Languages
License: Free to use but restricted distribution
Source0: Squeak2.7-src.tar.gz
Source1: Squeak2.7-aux.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Squeak is a graphical Smalltalk environment developed at Apple.

%prep
%setup -c -T -n squeak
%setup -q -D -T -a 0 -n squeak
%setup -q -D -T -a 1 -n squeak

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/squeak
mkdir $RPM_BUILD_ROOT/usr/local/bin/

install -m 0755 %{sparc_arch}/squeak $RPM_BUILD_ROOT/usr/local/bin
for i in %{sparc_arch}/*.so ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/lib/squeak
done
for i in Squeak2.7.changes Squeak2.7.image SqueakV2.sources ; do
    install -m 0644 $i $RPM_BUILD_ROOT/usr/local/lib/squeak
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To use Squeak, you have to make a directory with copies of the changes
and image files located in /usr/local/lib/squeak.  You also have to
make links to the sources file and the shared objects.
EOF

%files
%defattr(-,bin,bin)
%doc ReadMe.txt
/usr/local/bin/squeak
/usr/local/lib/*
