Name: infozip
Version: 2.3
Release: 6
Summary: Unix PKzip tools
Group: System Environment/Tools
Copyright: Freely distributable
Source0: zip23.tar.gz
Source1: unzip551.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Info-ZIP is a set of utilities that compress and package files; it is
compatible with the popular MS-DOS PKzip utility.

%prep
%setup -q -c -T -n zip
%setup -q -D -T -n zip -a 0
%setup -q -D -T -n zip -a 1

%build
cd zip-2.3
make -f unix/Makefile solaris_gcc
cd ../unzip-5.51
make -f unix/Makefile solaris CC=gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/bin

cd unzip-5.51
for i in unzip funzip unzipsfx ; do 
    install -c -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin/$i
done
install -c -m 0755 unix/zipgrep $RPM_BUILD_ROOT/usr/local/bin/zipgrep
for i in funzip unzip unzipsfx zipgrep zipinfo ; do
    install -c -m 0644 man/$i.1 $RPM_BUILD_ROOT/usr/local/man/man1/$i.1
done

cd ../zip-2.3
for i in zip zipnote zipsplit zipcloak ; do
    install -c -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin/$i
done
install -c -m 0444 man/zip.1 $RPM_BUILD_ROOT/usr/local/man/man1/zip.1

cd $RPM_BUILD_ROOT/usr/local/bin
ln -s unzip zipinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc unzip-5.51/LICENSE
/usr/local/bin/*
/usr/local/man/man1/*


