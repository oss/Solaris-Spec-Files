Name: tar
Version: 1.13.25
Copyright: GPL
Group: System Environment/Base
Summary: GNU tar
Release: 4
Requires: gzip bzip2
Source: tar-1.13.25.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU tar lets you create archives of several files.  It's a lot like Sun
tar, but it has a few more features.  Install this rpm if you want the
extra functionality of GNU tar.

%prep
%setup -q

%build
%ifarch sparc64
%configure64 --prefix=/usr/local/gnu
%else
%configure32 --prefix=/usr/local/gnu
%endif

%make

echo test > testfile
echo Testing gzip support...
./src/tar zcvf /dev/null testfile
echo Testing bzip2 support...
./src/tar jcvf /dev/null testfile

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu/bin
mkdir -p %{buildroot}/usr/local/bin
gmake install DESTDIR=%{buildroot}
cd %{buildroot}
ln -s usr/local/bin/tar usr/local/gnu/bin/tar 
ln -s usr/local/bin/tar usr/local/bin/gtar
rm usr/local/info/dir

%clean
rm -rf %{buildroot}

%post
%addinfo tar

%preun
%delinfo tar

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/info/tar.info*
/usr/local/gnu/bin/tar
/usr/local/bin/tar
/usr/local/bin/gtar
/usr/local/libexec/rmt