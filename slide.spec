Name: slide
Version: 1.0
Release: 3
Summary: execute a command as the super-user
Group: System Environment/Base
License: Rutgers
Source0: slide.tar.gz
Source1: slidepath.tar.gz
Patch: slide-mkfile.patch
BuildRoot: /var/tmp/%{name}-root

%description
Slide executes a command as the superuser.

%prep
%setup -T -c -n slide
%setup -q -D -T -b 0 -n slide
%setup -T -D -a 1 -n slide
cd latest/src
rm -rf RCS
cd ../..
%patch

%build
cd latest/src

make CC=gcc

%install
cd latest/src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/etc
cp slide $RPM_BUILD_ROOT/usr/local/bin/nslide
cp jrslide $RPM_BUILD_ROOT/usr/local/bin/jrslide
cp slide.1 $RPM_BUILD_ROOT/usr/local/man/man1
cp ../../slidepath $RPM_BUILD_ROOT/etc
cd $RPM_BUILD_ROOT/usr/local/bin
ln -s nslide slide

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/local/bin/slide
%attr(4711, root,staff) /usr/local/bin/nslide
%attr(4711, root,staff) /usr/local/bin/jrslide
%attr(755, root, staff) /etc/slidepath
/usr/local/man/man1/slide.1


